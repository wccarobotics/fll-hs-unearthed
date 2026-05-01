from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):

    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(241, then=Stop.COAST)
    drive_base.turn(55)
    drive_base.straight(139)
    drive_base.turn(-45)
    drive_base.straight(145)
    drive_base.turn(7)
    drive_base.straight(50)
    drive_base.turn(-41)
    drive_base.turn(15)
    drive_base.straight(1250)


