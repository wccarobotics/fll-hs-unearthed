from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
    
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(890)
    drive_base.turn(-90)
    drive_base.straight(-90)
    drive_base.turn(90)
    drive_base.straight(50)
    right_attachment.run(-450)
    wait(3000)
    drive_base.settings(straight_speed=900)
    drive_base.straight(-50)
    drive_base.turn(-90)
    drive_base.straight(120)
    drive_base.turn(85)
    drive_base.straight(-900)
