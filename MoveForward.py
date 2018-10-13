from MoveLegRear import MoveLegRear
from LegsControl import *
from MoveLegFront import MoveLegFront


def MoveStepForward(front_left, front_right, rear_left, rear_right):
    fL = MoveLegFront(front_left)
    rR = MoveLegRear(rear_right)
    fL.start()
    rR.start()
    time.sleep(h1_moving_angle * DELAY)
    fR = MoveLegFront(front_right)
    rL = MoveLegRear(rear_left)
    fR.start()
    rL.start()

    time.sleep(5)
    fL.shutdown()
    rR.shutdown()
    fR.shutdown()
    rL.shutdown()

