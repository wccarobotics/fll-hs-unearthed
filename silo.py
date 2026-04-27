from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):

    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(400)
    left_attachment.run_angle(5000, 200)
    left_attachment.run_angle(500, -200)
    left_attachment.run_angle(5000, 200)
    left_attachment.run_angle(500, -200)
    left_attachment.run_angle(5000, 200)
    left_attachment.run_angle(500, -200)
    left_attachment.run_angle(5000, 200)
    drive_base.settings(straight_speed=900)
    left_attachment.run_angle(500, -200)
    drive_base.straight(-400)


