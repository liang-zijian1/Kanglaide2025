import sys
import cv2
import numpy as np
import onnxruntime as ort
from networktables import NetworkTables
import time
import logging

# 初始化摄像头
def initialize_camera(gstreamer=False):
    if gstreamer:
        # 使用 GStreamer 管道初始化摄像头
        gstreamer_pipeline = (
            "v4l2src device=/dev/video0 ! "
            "image/jpeg, width=1280, height=720, framerate=30/1 ! "
            "jpegdec ! videoconvert ! appsink"
        )

        cap = cv2.VideoCapture(gstreamer_pipeline, cv2.CAP_GSTREAMER)
    else:
        cap = cv2.VideoCapture(0)  # 0 表示系统默认摄像头
        if not cap.isOpened():
            print("Failed to open camera.")
            exit()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_EXPOSURE, -4.5) 
    return cap

# 初始化网络表
def initialize_network_tables(server_address):
    logging.basicConfig(level=logging.DEBUG)
    NetworkTables.initialize(server=server_address)
    return NetworkTables.getTable('SmartDashboard')

# 显示 FPS
def display_fps(frame, start_time, show_fps):
    if show_fps:
        current_time = time.time()
        fps = 1 / (current_time - start_time)
        fps_text = f"FPS: {fps:.2f}"
        cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 找到最大的框
def find_largest_box(boxes, frame_width, frame_height, boundary_threshold,input_size):
    largest_box = None
    largest_area = 0

    for i in range(len(boxes)):
        center_x, center_y, width, height, score, angle_rad = boxes[i]
        confidence = score

        if confidence > 0.26:  # 置信度阈值
            center_x = int(center_x * (frame_width / input_size[0]))
            center_y = int(center_y * (frame_height / input_size[1]))
            width = int(width * (frame_width / input_size[0]))
            height = int(height * (frame_height / input_size[1]))

            box_points = cv2.boxPoints(((center_x, center_y), (width, height), np.degrees(angle_rad)))
            box_points = np.int32(box_points)

            x1, y1 = int(box_points[0][0]), int(box_points[0][1])
            x2, y2 = int(box_points[2][0]), int(box_points[2][1])

            if x1 < boundary_threshold or y1 < boundary_threshold or x2 > frame_width - boundary_threshold or y2 > frame_height - boundary_threshold:
                continue  # 跳过接触边界的框

            area = (x2 - x1) * (y2 - y1)
            if area > largest_area:
                largest_area = area
                largest_box = {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2,
                    "center_x": center_x,
                    "center_y": center_y,
                    "confidence": confidence,
                    "label": np.argmax([score])  # 获取类别 ID
                }

    return largest_box

# 实时推理函数
def real_time_inference(show_boxes=True, use_largest_box=True, show_fps=False):
    cap = initialize_camera(gstreamer=False)
    table = initialize_network_tables('10.2.54.2')
    
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_center_x = frame_width // 2
    video_center_y = frame_height // 2

    # 加载 ONNX 模型
    onnx_model_path = r"E:\Kanglaide2025\code\yolov8_training_4565\train_results_4565\weights\best.onnx"
    ort_session = ort.InferenceSession(onnx_model_path)

    BOUNDARY_THRESHOLD = 80  # 边界阈值

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        start_time = time.time()  # 开始推理计时

        # 将帧调整为模型输入尺寸
        
        input_size = (570, 570)
        frame_resized = cv2.resize(frame, input_size)
        frame_normalized = frame_resized / 255.0
        frame_input = np.transpose(frame_normalized, (2, 0, 1)).astype(np.float32)
        frame_input = np.expand_dims(frame_input, axis=0)

        # 推理当前帧
        ort_inputs = {ort_session.get_inputs()[0].name: frame_input}
        outputs = ort_session.run(None, ort_inputs)

        # 处理模型输出
        outputs = outputs[0][0]
        boxes = outputs[:6, :].transpose(1, 0)  # 转换为 (n, 6)

        # 找到最大的框（如果开关开启）
        largest_box = None
        if use_largest_box:
            largest_box = find_largest_box(boxes, frame_width, frame_height, BOUNDARY_THRESHOLD,input_size)

        x_offset = 0
        y_offset = 0

        # 绘制第一个满足置信度阈值的框
        for i in range(len(boxes)):
            center_x, center_y, width, height, score, angle_rad = boxes[i]
            confidence = score
            
            if confidence > 0.15:  # 置信度阈值
                center_x = int(center_x * (frame_width / input_size[0]))
                center_y = int(center_y * (frame_height / input_size[1]))
                width = int(width * (frame_width / input_size[0]))
                height = int(height * (frame_height / input_size[1]))

                box_points = cv2.boxPoints(((center_x, center_y), (width, height), np.degrees(angle_rad)))
                box_points = np.int32(box_points)

                x1, y1 = int(box_points[0][0]), int(box_points[0][1])
                x2, y2 = int(box_points[2][0]), int(box_points[2][1])

                if x1 < BOUNDARY_THRESHOLD or y1 < BOUNDARY_THRESHOLD or x2 > frame_width - BOUNDARY_THRESHOLD or y2 > frame_height - BOUNDARY_THRESHOLD:
                    continue  # 跳过接触边界的框

                # 计算偏移量并发送给网络表
                x_offset = center_x - video_center_x
                y_offset = center_y - video_center_y

                if show_boxes:
                    cv2.polylines(frame, [box_points], isClosed=True, color=(0, 0, 255), thickness=5)
                    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                    text = f"ID: {np.argmax([score])} {confidence:.2f}"
                    cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), thickness=2)
                break  # 找到第一个有效框后退出循环
            
        table.putNumber('x_offset', x_offset)
        table.putNumber('y_offset', y_offset)
        print(f"Sent x_offset: {x_offset}")
        print(f"Sent y_offset: {y_offset}")

        # 如果找到最大框，绘制并处理
        if largest_box:
            x1, y1, x2, y2 = largest_box["x1"], largest_box["y1"], largest_box["x2"], largest_box["y2"]
            center_x, center_y = largest_box["center_x"], largest_box["center_y"]
            confidence = largest_box["confidence"]

            if show_boxes:
                cv2.polylines(frame, [cv2.boxPoints(((center_x, center_y), (x2-x1, y2-y1), 0))], isClosed=True, color=(0, 255, 0), thickness=5)
                cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
                text = f"Max ID: {largest_box['label']} {confidence:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), thickness=2)

        display_fps(frame, start_time, show_fps)

        cv2.circle(frame, (video_center_x, video_center_y), 5, (255, 0, 0), -1)
        cv2.putText(frame, "Video Center", (video_center_x - 50, video_center_y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow('YOLO Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# 调用实时推理函数
real_time_inference(show_boxes=True, use_largest_box=True, show_fps=True)  # 设置 show_boxes 和 use_largest_box 为 True 或 False
