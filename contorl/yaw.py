from phoenix6.hardware import *
from phoenix6.controls import *

class Yaw:
    def __init__(self):
        self.yaw_motor = TalonFX(5)  # 旋转电机

        # 电机功率设置
        self.p = 0.2
        # 编码器限位
        self.left_position = 2.8   # 左限位置，2.1 转换为编码器单位
        self.right_position = -0.8  # 右限位置

    def control(self, left, right):
        """
        控制旋转角度：基于电机的编码器位置，控制电机的运动范围。
        :param left: 是否左转
        :param right: 是否右转
        """
        # 获取右电机当前编码器位置
        position = self.yaw_motor.get_position().value_as_double
        # print(right_position)
        # 判断是否超出限位并控制电机
        if left and position < self.left_position:
            # 左转未超过左限
            self.yaw_motor.set_control(DutyCycleOut(self.p))
        elif right and position > self.right_position:
            # 右转且未超过右限
            self.yaw_motor .set_control(DutyCycleOut(-self.p))
        else:
            # 超出限位或无输入，停止电机
            self.yaw_motor.set_control(DutyCycleOut(0))
         
            # self.right_pitch_motor.set_control(TorqueCurrentFOC(0.025))
        # 调试信息
        # print(f"Right Motor Position: {right_position:.2f}")

