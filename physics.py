import hal.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

class PhysicsEngine:
  def __init__(self, physics_controller):
    self.physics_controller = physics_controller

    self.lf_motor = hal.simulation.PWMSim(0)
    self.rf_motor = hal.simulation.PWMSim(1)

    bumper_width = 3.25 * units.inch

    self.drivetrain = tankmodel.TankModel.theory(
      motor_cfgs.MOTOR_CFG_CIM,           # motor configuration
      110 * units.lbs,                    # robot mass
      10.71,                              # drivetrain gear ratio
      2,                                  # motors per side
      22 * units.inch,                    # robot wheelbase
      23 * units.inch + bumper_width * 2, # robot width
      32 * units.inch + bumper_width * 2, # robot length
      6 * units.inch,                     # wheel diameter
    )

  def update_sim(self, now, tm_diff):
    # Simulate the drivetrain (only front motors used because read should be in sync)
    lf_motor = self.lf_motor.getSpeed()
    rf_motor = self.rf_motor.getSpeed()

    transform = self.drivetrain.calculate(lf_motor, rf_motor, tm_diff)
    pose = self.physics_controller.move_robot(transform)
