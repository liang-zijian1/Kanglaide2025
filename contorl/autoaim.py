from networktables import NetworkTables
from phoenix6.controls import *

class AutoAim:
    """管理自瞄功能的类（仅控制俯仰轴）"""

    def __init__(self, pitch,yaw, controller, table):
        self.pitch = pitch  # 俯仰电机
        self.yaw = yaw
        self.controller = controller  # 控制器
        self.table = table  # NetworkTables 表
        self.aiming_mode = False  # 初始状态为非自瞄模式
        self.previous_lb_state = False  # 记录上一次 LB 键的状态

        # 限位设定
        self.pitch_min_position = 0.6  # 俯仰电机最小位置
        self.pitch_max_position = 3.2  # 俯仰电机最大位置
        self.yaw_min_positon =-0.12
        self.yaw_max_positon =0.9
        self.dead_zone = 2 # 死区值，小于这个值的误差不再调整

        # 增量系数，用于控制每次调整的幅度
        self.k_pitch = 0.8  # Pitch 轴增量系数
        self.d_pitch = 0.08  # Pitch 轴的 D 控制系数
        self.k_yaw = 0.2
        self.d_yaw = 0.02
        # 上一次的误差值
        self.last_y_offset = 0
        self.last_x_offset = 0

    def toggle_aiming_mode(self):
        """切换自瞄模式"""
        current_lb_state = self.controller.getLeftBumper()
        if current_lb_state and not self.previous_lb_state:
            self.aiming_mode = not self.aiming_mode
            print(f"Aiming mode {'enabled' if self.aiming_mode else 'disabled'}")
        self.previous_lb_state = current_lb_state  # 更新 LB 按键状态

    def auto_aim(self):
        """执行自瞄调整逻辑（仅控制俯仰轴）"""
        if not self.aiming_mode:
            # 自瞄模式关闭时停止俯仰电机
            self.pitch.left_pitch_motor.set_control(DutyCycleOut(-0.014))
            self.pitch.right_pitch_motor.set_control(DutyCycleOut(0.014))
            self.yaw.yaw_motor.set_control(DutyCycleOut(0))
            return
        
        # 从 NetworkTables 获取 y_offset 偏移值
        y_offset = self.table.getNumber("y_offset", None)
        x_offset = self.table.getNumber("x_offset", None)

        # 如果没有检测到目标（y_offset 为 None 或 0），停止俯仰电机
        if y_offset is None or y_offset == 0 or x_offset is None or x_offset == 0:
            print("No target detected")
            self.pitch.left_pitch_motor.set_control(DutyCycleOut(-0.014))
            self.pitch.right_pitch_motor.set_control(DutyCycleOut(0.014))
            self.yaw.yaw_motor.set_control(DutyCycleOut(0))
            return
        
    
            

        # 死区过滤：如果 y_offset 偏移量小于阈值，停止调整
        if abs(y_offset) < self.dead_zone:
            self.pitch.left_pitch_motor.set_control(DutyCycleOut(-0.014))
            self.pitch.right_pitch_motor.set_control(DutyCycleOut(0.014))
            return
        
        if abs(x_offset) < self.dead_zone:
            self.yaw.yaw_motor.set_control(DutyCycleOut(0))

        # 计算增量调整量
        pitch_increment = y_offset * self.k_pitch
        yaw_increment = x_offset * self.k_yaw

        # 计算微分项，用于抑制震荡
        pitch_d_term = self.d_pitch * (y_offset - self.last_y_offset)
        yaw_d_term = self.d_yaw * (x_offset - self.last_x_offset)

        # 将增量和微分项结合到控制指令中
        pitch_adjustment = pitch_increment + pitch_d_term
        yaw_adjustment = yaw_increment + yaw_d_term

        # 更新误差值，供下次微分计算
        self.last_y_offset = y_offset
        self.last_x_offset = x_offset

        # 获取当前俯仰电机的位置
        current_pitch_position = self.pitch.right_pitch_motor.get_position().value_as_double
        current_yaw_position = self.yaw.yaw_motor.get_position().value_as_double

        # 增量调整电机位置
        new_pitch_position = current_pitch_position - pitch_adjustment
        new_yaw_position = current_yaw_position - yaw_adjustment
        # print(new_pitch_position)
        print("fuck",new_yaw_position)

        # 检查限位，防止电机超出设定的范围
        
        if (self.pitch_min_position <= current_pitch_position <= self.pitch_max_position)&(abs(y_offset)<400):
            if new_pitch_position>0:
                self.pitch.left_pitch_motor.set_control(DutyCycleOut(-new_pitch_position*0.00018))
                self.pitch.right_pitch_motor.set_control(DutyCycleOut(new_pitch_position*0.00018))
            if new_pitch_position<0:
                self.pitch.left_pitch_motor.set_control(DutyCycleOut(-new_pitch_position*0.00009))
                self.pitch.right_pitch_motor.set_control(DutyCycleOut(new_pitch_position*0.00009))
        if self.pitch_min_position>=current_pitch_position:
            print("Pitch motor at limit, adjustment skipped")
            self.pitch.left_pitch_motor.set_control(DutyCycleOut(-0.035))
            self.pitch.right_pitch_motor.set_control(DutyCycleOut(0.035))
        if current_pitch_position>= self.pitch_max_position:
            self.pitch.left_pitch_motor.set_control(DutyCycleOut(0.015))
            self.pitch.right_pitch_motor.set_control(DutyCycleOut(-0.015))
        
        if (self.yaw_min_positon <= current_yaw_position <= self.yaw_max_positon)&(abs(x_offset)<400):
            if new_yaw_position>0:
                self.yaw.yaw_motor.set_control(DutyCycleOut(new_yaw_position*0.0018))
            if new_yaw_position<0:
                self.yaw.yaw_motor.set_control(DutyCycleOut(new_yaw_position*0.0018))
        if self.yaw_min_positon>=current_yaw_position:
            print("Yaw motor at limit, adjustment skipped")
            self.yaw.yaw_motor.set_control(DutyCycleOut(0))
        if current_yaw_position>= self.yaw_max_positon:
            self.yaw.yaw_motor.set_control(DutyCycleOut(0))
            
            
        # 调试输出
        print(f"y_offset: {y_offset},x_offset: {x_offset}")
        print(f"Pitch adjustment: {new_pitch_position},Yaw adjustment: {new_yaw_position}")
