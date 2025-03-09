#!/usr/bin/env python3.12
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
from shooter import Shooter  # 飞轮模块
from pitch import Pitch      # 俯仰角模块
from yaw import Yaw          # Yaw 模块
from autoaim import AutoAim  # 自瞄模块
from networktables import NetworkTables
import logging

class SimpleRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        初始化所有模块，包括手柄、自瞄、俯仰角和飞轮控制。
        """
        self.controller = wpilib.XboxController(0)  # 初始化xobx手柄
        # self.controller = wpilib.Joystick(4)#初始化其他类型手柄
        self.my_Shooter = Shooter()  # 飞轮控制模块
        self.my_Pitch = Pitch()      # 俯仰角控制模块
        self.my_Yaw = Yaw()          # 云台控制模块

        # 初始化 NetworkTables（自瞄传感器数据）
        logging.basicConfig(level=logging.DEBUG)
        NetworkTables.initialize(server='10.2.54.2')  # 替换为实际服务器地址
        self.table = NetworkTables.getTable('SmartDashboard')

        # 初始化自瞄模块
        self.auto_aim = AutoAim( self.my_Pitch, self.my_Yaw,self.controller, self.table)
    

    def teleopInit(self):
        """每次进入遥控模式时运行一次，初始化电机。"""
        #self.my_Pitch.motor_init()
        #self.my_Yaw.init_motor()

    def teleopPeriodic(self):
        """遥控模式下周期性运行的代码。"""
        # # 切换自瞄模式
        self.auto_aim.toggle_aiming_mode()

        if self.auto_aim.aiming_mode:
            # 自瞄模式：调整俯仰角度和飞轮速度
            self.auto_aim.auto_aim()
        else:
            # 手动模式：使用手柄控制飞轮和俯仰角
            # 控制飞轮速度
            right_trigger_value = self.controller.getRightTriggerAxis()  # 获取右扳机输入
            self.my_Shooter.control(right_trigger_value)
            # 控制俯仰角度
            self.my_Pitch.control(self.controller.getYButton(), self.controller.getAButton())
            self.my_Yaw.control(self.controller.getXButton(),self.controller.getBButton())
        

    def testInit(self):
        """测试模式初始化（如果需要）。"""

    def testPeriodic(self):
        """测试模式周期性运行（如果需要）。"""

    def disabledInit(self):
        """当机器人禁用时运行的代码（如果需要）。"""

if __name__ == "__main__":
    wpilib.run(SimpleRobot)
