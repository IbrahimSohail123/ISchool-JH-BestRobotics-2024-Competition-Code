# Write your code here :-)
#MOTOR
import time
import circuitpython_gizmo
import pwmio
import adafruit_motor
from adafruit_motor import servo
from adafruit_simplemath import map_range, constrain

gizmo = circuitpython_gizmo.Gizmo()
servo1 = adafruit_motor.servo.Servo(
    pwmio.PWMOut(gizmo.SERVO_1, frequency=50),
    actuation_range=90,
    min_pulse=1000,
    max_pulse=2000
)
servo2 = adafruit_motor.servo.Servo(
    pwmio.PWMOut(gizmo.SERVO_2, frequency=50),
    actuation_range=90,
    min_pulse=1000,
    max_pulse=2000
)
servo3 = adafruit_motor.servo.Servo(
    pwmio.PWMOut(gizmo.SERVO_3, frequency=50),
    actuation_range=90,
    min_pulse=1000,
    max_pulse=2000
)

servo4 = adafruit_motor.servo.Servo(
    pwmio.PWMOut(gizmo.SERVO_4, frequency=50),
    actuation_range=90,
    min_pulse=1000,
    max_pulse=2000
)

motor1 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_1, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)
motor2 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_2, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)
motor3 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_3, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)
motor4 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_4, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)

####################################################################
while True:
    gizmo.refresh()
    if gizmo.buttons.a:
        print("A: %s" % gizmo.buttons.a)
        motor1.throttle = 1.0
    else:
        motor1.throttle = 0.0

    if gizmo.buttons.b:
        print("B: %s" % gizmo.buttons.b)
        motor2.throttle = 1.0
    else:
        motor2.throttle = 0.0

    # Convert gamepad axis positions (0 - 255) to motor speeds (-1.0 - 1.0)
    motor3.throttle = map_range(gizmo.axes.left_y, 0, 255, -1.0, 1.0)
    motor4.throttle = map_range(gizmo.axes.right_y, 0, 255, -1.0, 1.0)
    #print("LEFT Y: %s" % map_range(gizmo.axes.left_y, 0, 255, -1.0, 1.0))
    #print("RIGHT Y: %s" % map_range(gizmo.axes.right_y, 0, 255, -1.0, 1.0))

    if gizmo.buttons.a:
        print("A: %s" % gizmo.buttons.x)
        motor2.throttle = 1.0
        time.sleep(0.05)
        motor2.throttle = 0.0
        time.sleep(0.5)
    elif gizmo.buttons.b:
        print("B: %s" % gizmo.buttons.y)
        motor2.throttle = -1.0
        time.sleep(0.05)
        motor2.throttle = 0.0
        time.sleep(0.5)
    else:
        motor2.throttle = 0.0

    if gizmo.buttons.x:
        print("X: %s" % gizmo.buttons.x)
        motor1.throttle = 1.0
    elif gizmo.buttons.y:
        print("Y: %s" % gizmo.buttons.y)
        motor1.throttle = -1.0
    else:
        motor1.throttle = 0.0

    #SERVOS######################################
    #if gizmo.buttons.y:
    #    print("Y: %s" % gizmo.buttons.y)
    #    motor4.throttle = 1.0
    #else:
    #    motor4.throttle = 0.0

    #if gizmo.buttons.y:
    #    print("Y: %s" % gizmo.buttons.y)
    #    motor4.throttle = 1.0
    #else:
    #    motor4.throttle = 0.0

    #if gizmo.buttons.y:
    #    print("Y: %s" % gizmo.buttons.y)
    #    motor4.throttle = 1.0
    #else:
    #    motor4.throttle = 0.0

    #if gizmo.buttons.y:
    #    print("Y: %s" % gizmo.buttons.y)
    #    motor4.throttle = 1.0
    #else:
    #    motor4.throttle = 0.0
    #
    time.sleep(0.1)
