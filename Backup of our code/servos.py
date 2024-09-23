import time
import circuitpython_gizmo
import pwmio
import adafruit_motor
from adafruit_motor import servo

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

while True:
    gizmo.refresh()
    print("A: %s" % gizmo.buttons.a)
    print("B: %s" % gizmo.buttons.b)
    if gizmo.buttons.a:
        servo1.angle = 90
    else:
        servo1.angle = 0

    if gizmo.buttons.b:
        servo2.angle = 90
    else:
        servo2.angle = 0
    time.sleep(0.1)
