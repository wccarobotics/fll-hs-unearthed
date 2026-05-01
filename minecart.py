from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):



   
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(770)
    drive_base.arc(59, angle=85)
    drive_base.straight(80)
    left_attachment.run_angle(200, -160)
    wait(500)
    left_attachment.run_angle(500, -50)
    drive_base.turn(45)
    left_attachment.run_angle(200, 210)
    drive_base.straight(150)
    drive_base.turn(16)
    drive_base.straight(55)
    left_attachment.run_angle(185, -60)
    drive_base.turn(-22)
    drive_base.straight(-95)
    left_attachment.run_angle(200, -80)
    drive_base.straight(-50)
    drive_base.turn(-90)
    drive_base.straight(-810)

