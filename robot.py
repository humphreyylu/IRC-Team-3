import wpilib

class MyRobot(wpilib.TimedRobot):
  def robotInit(self):
    self.left_drive_motors = wpilib.VictorSP(0)
    self.right_drive_motors = wpilib.VictorSP(1)
    self.right_drive_motors.setInverted(True)

    self.left_joystick = wpilib.Joystick(0)
    self.right_joystick = wpilib.Joystick(1)

  def autonomousInit(self):
    self.timer = wpilib.Timer()
    self.timer.start()
  def autonomousPeriodic(self):
    if self.timer.get() < 1:
      self.left_drive_motors.set(1)
      self.right_drive_motors.set(1)
    else:
      self.left_drive_motors.set(0)
      self.right_drive_motors.set(0)




  def teleopPeriodic(self):
    self.left_drive_motors.set(self.left_joystick.getY())
    self.right_drive_motors.set(self.right_joystick.getY())

if __name__ == '__main__':
  wpilib.run(MyRobot)