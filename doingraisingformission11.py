from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
        drive_base.use_gyro(True)
        drive_base.settings(straight_speed=900)
        drive_base.straight(1055)
        drive_base.turn(90)
        drive_base.straight(75)
        drive_base.turn(-5)
        right_attachment.control.limits(acceleration=900)
        right_attachment.run(500)
        wait(3000)
        right_attachment.stop()
        drive_base.turn(16)
        drive_base.straight(-125)
        drive_base.turn(-105)
        drive_base.straight(-1050)
