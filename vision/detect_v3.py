import cv2
import torch
import numpy as np
from PIL import Image
import time
from ultralytics import YOLO
# 加载本地训练的 YOLOv8 模型
model = YOLO(r'E:\Kanglaide2025\code\yolov8_training_4565\train_results_4565\weights\best.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)  # 0 表示系统默认摄像头
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 设置摄像头分辨率（根据需要降低分辨率提高推理速度）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 跳帧计数器
frame_skip = 2  # 每隔 5 帧推理一次
frame_count = 0

# 主循环：捕获帧，发送到模型进行推理，显示结果
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法捕获帧")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        # 跳过推理，直接显示当前帧
        cv2.imshow("Real-Time Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    # 将帧转换为 RGB 图像
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    box_color = (0, 255, 0)  # 绿色
    # 使用 YOLOv8 进行推理
    results = model(rgb_frame)  # 传递帧进行推理
    text_color = (0, 0, 255)  # 红色
    # 在帧上绘制检测结果
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 检测框的左上角和右下角坐标
            confidence = box.conf[0]  # 置信度
            class_id = int(box.cls[0])  # 类别ID
            label = model.names[class_id]  # 获取类别名称

            # 绘制检测框
            cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, thickness=2)

            # 绘制标签
            text = f"{label} {confidence:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, thickness=2)

    # 显示处理后的帧
    cv2.imshow("Real-Time Detection", frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
