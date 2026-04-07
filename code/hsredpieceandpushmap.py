from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
    wait(200)
    drive_base.use_gyro(True)
    # Start 8 to the left tire
    drive_base.settings(straight_speed=900)
    drive_base.straight(675)
    drive_base.turn(-28)
    drive_base.straight(150)
    drive_base.straight(-120)
    drive_base.turn(35)
    drive_base.straight(-700, then=Stop.NONE)