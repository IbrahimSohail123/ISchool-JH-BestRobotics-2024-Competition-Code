import time
import circuitpython_gizmo
import pwmio
import adafruit_motor
from adafruit_motor import servo

gizmo = circuitpython_gizmo.Gizmo()

motor = adafruit_motor.servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_4, frequency=50),
    min_pulse=1000,
    max_pulse=2000
)

while True:
    gizmo.refresh()
    print("A: %s" % gizmo.buttons.a)
    if gizmo.buttons.a:
        motor.throttle = 1.0
    else:
        motor.throttle = 0.0
    time.sleep(0.1)

#    motor.throttle = 1.0
#    time.sleep(10)
#     motor.throttle = 0.5
#    time.sleep(10)
#    motor.throttle = 0
#    time.sleep(1)

