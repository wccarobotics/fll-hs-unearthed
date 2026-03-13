from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
    

# The main program starts here.
# The starting plase is the  secend square and the back line.
    drive_base.use_gyro(True)
    drive_base.straight(470)
    drive_base.straight(-175)
    drive_base.turn(40)
    drive_base.straight(475)
    drive_base.turn(-84)
    drive_base.settings(straight_speed=900)
    drive_base.straight(280)
    drive_base.straight(-150)
    drive_base.turn(75)
    drive_base.straight(-800)
