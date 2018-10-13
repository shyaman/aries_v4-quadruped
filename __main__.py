from LegsControl import *
from MoveForward import MoveStepForward

rear_left = RobotLeg(6, 5, m2_revert=2, servoMinOffset=-0.05)
rear_right = RobotLeg(10, 9, m2_revert=1, m1_revert=3, servoMaxOffset=-0.05, servoMinOffset=-0.25)
front_left = RobotLeg(3, 2, m2_revert=1, m1_revert=3, servoMinOffset=-0.15)
front_right = RobotLeg(11, 12, m2_revert=2, servoMinOffset=-0.05)

if __name__ == '__main__':

    KeepAlive()
    # rear_left.move_h1(MIN_h1_rear)
    # rear_right.move_h1(MIN_h1_rear)
    # front_left.move_h1(MAX_h1_front)
    # front_right.move_h1(MAX_h1_front)
    #
    # for x in range(-90, MAX_h2):
    #     rear_left.move_h2(x)
    #     rear_right.move_h2(x)
    #     front_left.move_h2(x)
    #     front_right.move_h2(x)
    #     time.sleep(3 * DELAY)

    while True:
        # desiredPosition1 = input("value1? ")
        desiredPosition2 = input("value2? ")

        MoveStepForward(front_left, front_right, rear_left, rear_right)

        # rear_left.move_h1(desiredPosition1)
        # rear_right.move_h1(desiredPosition1)
        #
        # rear_left.move_h2(desiredPosition2)
        # rear_right.move_h2(desiredPosition2)
        #
        # front_left.move_h1(desiredPosition1)
        # front_right.move_h1(desiredPosition1)
        #
        # front_left.move_h2(desiredPosition2)
        # front_right.move_h2(desiredPosition2)
        # pass
