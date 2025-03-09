from phoenix6.hardware import *
from phoenix6.controls import *

class Pitch:
    def __init__(self):
        self.left_pitch_motor = TalonFX(2)  # 左俯仰电机
        self.right_pitch_motor = TalonFX(1)  # 右俯仰电机

        # 电机功率设置
        self.u = 0.04  # 上升功率
        self.d = 0.018  # 下降功率

        # 编码器限位（基于右电机）
        self.max_position = 3.3   # 上限位置，2.1 转换为编码器单位
        self.min_position = 0.8  # 下限位置

    def control(self, up, down):
        """
        控制俯仰角度：基于右电机的编码器位置，控制左右电机的运动范围。
        :param up: 是否上升
        :param down: 是否下降
        """
        # 获取右电机当前编码器位置
        right_position = self.right_pitch_motor.get_position().value_as_double
        # print(right_position)
        # 判断是否超出限位并控制电机
        if up and right_position < self.max_position:
            # 上升且未超过上限
            self.left_pitch_motor.set_control(DutyCycleOut(-self.u))
            self.right_pitch_motor.set_control(DutyCycleOut(self.u))
        elif down and right_position > self.min_position:
            # 下降且未超过下限
            self.left_pitch_motor.set_control(DutyCycleOut(self.d))
            self.right_pitch_motor.set_control(DutyCycleOut(-self.d))
        else:
            # 超出限位或无输入，停止电机
            self.left_pitch_motor.set_control(DutyCycleOut(-0.014))
            self.right_pitch_motor.set_control(DutyCycleOut(0.014))
            # self.right_pitch_motor.set_control(TorqueCurrentFOC(0.025))
        # 调试信息
        # print(f"Right Motor Position: {right_position:.2f}")

