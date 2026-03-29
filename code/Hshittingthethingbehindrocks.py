from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
import robot


def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
 
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(250)
    drive_base.arc(100, angle=35)
    drive_base.straight(240)
    drive_base.arc(-100, angle=35)
    drive_base.straight(240)
    drive_base.turn(-30)
    drive_base.settings(straight_speed=900)
    drive_base.straight(65)
    drive_base.turn(45)
    drive_base.turn(-21)
    drive_base.straight(-350)
