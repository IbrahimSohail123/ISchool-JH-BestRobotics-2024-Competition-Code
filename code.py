# ISUP Primary Code
#MOTOR
import time
import circuitpython_gizmo
import pwmio
import adafruit_motor
from adafruit_motor import servo
from adafruit_simplemath import map_range, constrain

gizmo = circuitpython_gizmo.Gizmo()
#Pez Dispenser
servo1 = adafruit_motor.servo.Servo(pwmio.PWMOut(gizmo.SERVO_1, frequency=50))

#Currently Not In Use
servo2 = adafruit_motor.servo.Servo(pwmio.PWMOut(gizmo.SERVO_2, frequency=50))

#servo3 = adafruit_motor.servo.Servo(
#    pwmio.PWMOut(gizmo.SERVO_3, frequency=50),
#    actuation_range=90,
#    min_pulse=1000,
#    max_pulse=2000
#)
#
#servo4 = adafruit_motor.servo.Servo(
#    pwmio.PWMOut(gizmo.SERVO_4, frequency=50),
#    actuation_range=90,
#    min_pulse=1000,
#    max_pulse=2000
#)

#Med Motor - Arm Rotate
motor1 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_1, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)
#Med Motor - Arm Up and Down
motor2 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_2, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)
#Large Motor - Left Wheel
motor3 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_3, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)
#Large Motor - Right Wheel
motor4 = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_4, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)

####################################################################
#Starting Position - Pez Dispenser
servo1.angle = 120

####################################################################
while True:
    gizmo.refresh()
    #JOYSTICKS
    motor3.throttle = map_range(gizmo.axes.left_y, 0, 255, -1.0, 1.0)
    motor4.throttle = map_range(gizmo.axes.right_y, 0, 255, -1.0, 1.0)

    #ARM UP / DOWN
    if gizmo.buttons.y:
        print("X: %s" % gizmo.buttons.x)
        motor2.throttle = 1.0
    elif gizmo.buttons.a:
        print("Y: %s" % gizmo.buttons.y)
        motor2.throttle = -1.0
    else:
        motor2.throttle = 0.0

    #ARM ROTATE
    if gizmo.buttons.x:
        print("A: %s" % gizmo.buttons.x)
        motor1.throttle = 1.0
        time.sleep(0.05)
        motor1.throttle = 0.0
        time.sleep(0.1)
    elif gizmo.buttons.b:
        print("B: %s" % gizmo.buttons.y)
        motor1.throttle = -1.0
        time.sleep(0.05)
        motor1.throttle = 0.0
        time.sleep(0.1)
    else:
        motor1.throttle = 0.0


    #SERVOS######################################
    #Pez Dispenser
    if gizmo.buttons.left_trigger:
        print("left_trigger: %s" % gizmo.buttons.left_trigger)
        #servo1.angle = 0
        
        for angle in range(120, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            servo1.angle = angle
            time.sleep(0.05)
        time.sleep(0.5)
        servo1.angle = 120
    #else:
        #servo1.angle = 120

    #if gizmo.buttons.right_shoulder:
    #    servo2.angle = 90
    #elif gizmo.buttons.right_trigger:
    #    servo2.angle = 180

    time.sleep(0.1)