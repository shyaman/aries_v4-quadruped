from LegsControl import *
import time


def SlowStepForward(front_left, front_right, rear_left, rear_right, Factor = 0.0):
    front_left_r = Process(target=FrontLeg, args=(front_left,Factor,))
    rear_right_r = Process(target=RearLeg,args=(rear_right,Factor,))
    front_left_r.start()
    rear_right_r.start()
    time.sleep(h1_moving_angle * DELAY)
    front_right_r = Process(target=FrontLeg, args=(front_right,Factor,))
    rear_left_r = Process(target=RearLeg, args=(rear_left,Factor,))
    front_right_r.start()
    rear_left_r.start()
    front_left_r.join()
    rear_right_r.join()
    front_right_r.join()
    rear_left_r.join()


def FrontLeg(leg,Factor = 0):
    leg.move_h2(MIN_h2)

    for x in range(MAX_h1_front, int(MAX_h1_front*(1-Factor)), -1):
        leg.move_h1(x)
        time.sleep(DELAY)

    leg.move_h2(MAX_h2)
    for x in range(int(MAX_h1_front*(1-Factor)), MAX_h1_front):
        leg.move_h1(x)
        time.sleep(DELAY)


def RearLeg(leg, Factor = 0):
    leg.move_h2(MIN_h2)

    for x in range(MIN_h1_rear, int(MIN_h1_rear*(1+Factor))):
        leg.move_h1(x)
        time.sleep(DELAY)

    leg.move_h2(MAX_h2)
    for x in range(int(MIN_h1_rear*(1+Factor)), MIN_h1_rear, -1):
        leg.move_h1(x)
        time.sleep(DELAY)
