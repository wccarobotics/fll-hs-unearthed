from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):

    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.straight(600)
    drive_base.arc(59, angle=60)
    drive_base.straight(160)
    left_attachment.run_angle(200, -360)
    drive_base.turn(45)
    left_attachment.run_angle(200, 360)
    drive_base.straight(50)
    drive_base.turn(25)
    drive_base.straight(60)
    left_attachment.run_angle(-150, 100)
    prime_hub.speaker.beep(500, 125)
    drive_base.turn(-20)
    left_attachment.run_angle(-150, 200)
    drive_base.straight(-300)
    drive_base.turn(80)
    drive_base.settings(straight_speed=500)
    drive_base.straight(700)