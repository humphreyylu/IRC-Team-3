import wpilib
import wpilib.drive

class MyRobot(wpilib.TimedRobot):
  def robotInit(self):
    pass

if __name__ == '__main__':
  wpilib.run(MyRobot)
