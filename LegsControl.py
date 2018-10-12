import time
import navio.pwm
import navio.util

navio.util.check_apm()

SERVO_MIN = 0.700  # ms
SERVO_MAX = 1.500  # ms
PERIOD = 50

MAX_h1_front = 90
MAX_h1_rear = 130
h1_moving_angle = 70
MIN_h1_front = MAX_h1_front - h1_moving_angle
MIN_h1_rear = MAX_h1_rear - h1_moving_angle

MAX_h2 = 65

DELAY = 0.01

PWM_UNUSED = 8


class RobotLeg:
    def __init__(self, m1, m2, m1_revert=0, m2_revert=0, servoMaxOffset=0, servoMinOffset=0):
        self.h1 = navio.pwm.PWM(m1)
        self.h2 = navio.pwm.PWM(m2)
        self.h1_revert = m1_revert
        self.h2_revert = m2_revert
        self.servoMaxOffset = servoMaxOffset
        self.servoMinOffset = servoMinOffset

        # initializing
        self.h1.initialize()
        self.h2.initialize()

        # setting period
        self.h1.set_period(PERIOD)
        self.h2.set_period(PERIOD)

        # enable pwm
        self.h1.enable()
        self.h2.enable()

    def move_h1(self, angle):
        self.h1.set_duty_cycle(self.degreeToDuty(angle, revert=self.h1_revert))

    def move_h2(self, angle):
        self.h2.set_duty_cycle(self.degreeToDuty(angle, revert=self.h2_revert))

    def degreeToDuty(self, degree, revert):
        if revert == 1:
            return (((SERVO_MAX - SERVO_MIN + self.servoMaxOffset - self.servoMinOffset) / 90.) * degree) + SERVO_MAX \
                   + self.servoMaxOffset
        if revert == 2:
            return SERVO_MAX - (((SERVO_MAX - SERVO_MIN + self.servoMaxOffset - self.servoMinOffset) / 90.) * degree) \
                   + self.servoMaxOffset
        if revert == 3:
            return (((SERVO_MAX - SERVO_MIN + self.servoMaxOffset - self.servoMinOffset) / 90.) * (90 - degree)) \
                   + SERVO_MAX + self.servoMaxOffset
        else:
            return (((SERVO_MAX - SERVO_MIN + self.servoMaxOffset - self.servoMinOffset) / 90.) * degree) + SERVO_MIN \
                   + self.servoMinOffset


def moveLegFront(leg, delay=0):
    # time.sleep(delay)
    while True:

        leg.move_h2(MAX_h2 / 1.5)
        for x in range(MAX_h1_front, MIN_h1_front, -1):
            leg.move_h1(x)
            time.sleep(DELAY)

        leg.move_h2(MAX_h2)
        for x in range(MIN_h1_front, MAX_h1_front):
            leg.move_h1(x)
            time.sleep(DELAY)


def moveLegRear(leg, delay=0):
    # time.sleep(delay)
    while True:

        leg.move_h2(MAX_h2 / 1.5)
        for x in range(MIN_h1_rear, MAX_h1_rear):
            leg.move_h1(x)
            time.sleep(DELAY)

        leg.move_h2(MAX_h2)
        for x in range(MAX_h1_rear, MIN_h1_rear, -1):
            leg.move_h1(x)
            time.sleep(DELAY)


def keepAlive():
    unused = navio.pwm.PWM(PWM_UNUSED)
    unused.initialize()
    unused.set_period(PERIOD)
    unused.enable()

    while True:
        unused.set_duty_cycle(0.001)
        time.sleep(DELAY)


def keepAliveThread():
    try:
        KA = multiprocessing.Process(target=keepAlive)
        KA.start()
    except:
        print "Error: unable to start thread"
