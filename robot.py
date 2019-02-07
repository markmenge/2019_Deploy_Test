#GENERAL PYTHON
import math

#GENERAL ROBOT
import ctre 
import wpilib

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        #assigns driver as controller 0 and operator as controller 1
        # self.driver = wpilib.XboxController(0)
        # self.operator = wpilib.XboxController(1)
        self.master_talon = ctre.WPI_TalonSRX(1)
        self.master_talon = ctre.WPI_TalonSRX(4)
        pass


    def robotPeriodic(self):
        pass

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        pass

    def teleopPeriodic(self):
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)