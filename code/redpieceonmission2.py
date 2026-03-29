from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
            
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(650, then=Stop.COAST)
    drive_base.turn(-45)
    drive_base.straight(60)
    drive_base.straight(-50)
    drive_base.turn(40)
    drive_base.straight(-650)
