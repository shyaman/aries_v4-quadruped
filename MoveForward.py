from LegsControl import *
import multiprocessing


def movePairOne(frontLeg, rearLeg):
    try:
        fl = multiprocessing.Process(target=moveLegFront, args=(frontLeg,))
        rl = multiprocessing.Process(target=moveLegRear, args=(rearLeg, MAX_h1_front / 3 * DELAY))
        fl.start()
        rl.start()
    except:
        print "Error: unable to start thread"


def MoveStepForward(front_left, front_right, rear_left, rear_right):
    movePairOne(front_left, rear_right)
    time.sleep(h1_moving_angle * DELAY)
    movePairOne(front_right, rear_left)
