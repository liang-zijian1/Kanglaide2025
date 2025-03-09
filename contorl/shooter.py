from phoenix6.hardware import TalonFX  # 如果使用的是 TalonSRX 或 TalonFX，替换为实际类型
from phoenix6.controls import DutyCycleOut,NeutralOut

class Shooter:
    def __init__(self):
        self.left_flywheel = TalonFX(3)   # 左飞轮电机
        self.right_flywheel = TalonFX(4)  # 右飞轮电机

    def control(self, button):
        """
        控制左右飞轮速度
        :param left_speed: 左飞轮速度 (0~1)
        :param right_speed: 右飞轮速度 (0~1)
        """
        self.speed=0.3
        if(button):
            self.left_flywheel.set_control(DutyCycleOut(-self.speed))
            self.right_flywheel.set_control(DutyCycleOut(self.speed))
        else:
            self.left_flywheel.set_control(NeutralOut())
            self.right_flywheel.set_control(NeutralOut())
            