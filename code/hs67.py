from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, prime_hub: PrimeHub):
    drive_base.use_gyro(True)
    wait(200)
    # start on back line near mission 11
    # bottom left of yellow box
    # wheel on the 3rd line from the big black
    # line!  Bottom left of the yellow box.
    # line is 2 over from bottom of yellow box.
    # Make sure it is right and carful when pushing button!
    # Doing mission 6
    drive_base.settings(straight_speed=900)
    drive_base.straight(550)
    right_attachment.run_angle(500, -190)
    drive_base.straight(190)
    # Doing Mission 5.
    drive_base.turn(-45)
    drive_base.straight(60)
    drive_base.settings(straight_speed=200)
    drive_base.turn(-30)
    drive_base.straight(-60)
    drive_base.turn(-15)
    # Leaving missions
    drive_base.settings(straight_speed=460)
    drive_base.straight(500)
    # tern torward scale
    drive_base.settings(straight_speed=900)
    drive_base.turn(-90)
    # Doing mission 10
    drive_base.settings(straight_speed=150)
    drive_base.straight(-155)
    drive_base.turn(-48)
    drive_base.settings(straight_speed=700)
    drive_base.straight(340)
    drive_base.straight(-200)
    drive_base.turn(-22.5, then=Stop.NONE)
    drive_base.settings(straight_speed=900)
    drive_base.straight(350)
    right_attachment.run_angle(500, 190)
    drive_base.turn(-18)
    drive_base.straight(300, then=Stop.COAST)
    drive_base.straight(-300)
    drive_base.turn(78)
    drive_base.settings(straight_speed=900)
    drive_base.straight(650)
    drive_base.settings(straight_speed=200)



# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(robot.drive_base, robot.left_attachment, robot.right_attachment)