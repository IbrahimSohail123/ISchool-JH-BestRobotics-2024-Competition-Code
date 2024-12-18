"""
This is the default BEST Robotics program for the Gizmo.
This program offers remote control of simple robots using 3 motors and a servo.
This may serve as a useful starting point for your team's competition code. You
will almost certainly need to edit or extend this code to meet your needs.

This code has two control modes: 'Tank Mode' and 'Arcade Mode'. The Start
button on your gamepad switches the robot between the two modes.

Here are the controls for Tank Mode:
Left Joystick Up/Down    - Motor 1 Fwd/Rev
Right Joystick Up/Down   - Motor 3 Fwd/Rev

Here are the controls for Arcade Mode:
Left Joystick Up/Down    - Robot Fwd/Rev
Left Joystick Left/Right - Robot Turn Left/Right

These controls work in both modes:
Right Trigger            - Motor 4 Forward
Right Shoulder Button    - Motor 4 Reverse
Left Trigger             - Servo 1 to 0 degrees
Left Shoulder Button     - Servo 1 to 90 degrees

When neither the left trigger nor shoulder button are pressed, the servo will
go to 45 degrees.
"""

import time
import board
import pwmio
import digitalio
from adafruit_motor import servo
from adafruit_simplemath import map_range, constrain
from circuitpython_gizmo import Gizmo

# the Gizmo object provides access to the data that is held by the field
# management system and the gizmo system processor
gizmo = Gizmo()

pwm_freq = 50 # Hertz
min_pulse = 1000 # milliseconds
max_pulse = 2000 # milliseconds
servo_range = 90  # degrees

# Configure the motors & servos for the ports they are connected to
#MOTORS
motor_left= servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_4, frequency=pwm_freq),
    min_pulse=min_pulse,
    max_pulse=max_pulse
)
motor_right = servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_3, frequency=pwm_freq),
    min_pulse=min_pulse,
    max_pulse=max_pulse
)
motor_arm_base = servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_2, frequency=pwm_freq),
    min_pulse=min_pulse,
    max_pulse=max_pulse
)
motor_arm_updown = servo.ContinuousServo(
    pwmio.PWMOut(gizmo.MOTOR_1, frequency=pwm_freq),
    min_pulse=min_pulse,
    max_pulse=max_pulse
)

#SERVOS
servo_box_stacker = servo.Servo(
    pwmio.PWMOut(gizmo.SERVO_1, frequency=pwm_freq),
    actuation_range=servo_range,
    min_pulse=min_pulse,
    max_pulse=max_pulse
)
TANK_MODE = 0
ARCADE_MODE = 1

mode = ARCADE_MODE

prev_start_button = False

# Keep running forever
while True:
    # Toggle the built-in LED each time through the loop so we can see
    # that the program really is running.
    #builtin_led.value = not builtin_led.value

    # Refreshes the information about axis and button states
    gizmo.refresh()

    # If the start button was pressed, switch control mode
    if gizmo.buttons.start and not prev_start_button:
        if mode == TANK_MODE:
            mode = ARCADE_MODE
        elif mode == ARCADE_MODE:
            mode = TANK_MODE
    prev_start_button = gizmo.buttons.start

    # Fix the mode to ARCADE_MODE and ignore the start button
    mode = ARCADE_MODE
    if mode == ARCADE_MODE:
        # Convert gamepad axis positions (0 - 255) to motor speeds (-1.0 - 1.0)
        motor_left.throttle = map_range(gizmo.axes.left_y, 0, 255, -1.0, 1.0)
        print('Left Y: ' + str(gizmo.axes.left_y))
        motor_right.throttle = map_range(gizmo.axes.right_y, 0, 255, -1.0, 1.0)
        print('Right Y: ' + str(gizmo.axes.right_y))
    elif mode == TANK_MODE:
        # Mix right joystick axes to control both wheels
        print('Left X: ' + str(gizmo.axes.left_x) + ', Left Y: ' + str(gizmo.axes.left_y))
        speed = map_range(gizmo.axes.left_y, 0, 255, 1.0, -1.0)
        steering = map_range(gizmo.axes.left_x, 0, 255, -1.0, 1.0)
        print('Speed: ' + str(speed) + ', Steering: '+str(steering))
        motor_left.throttle = constrain(speed - steering, -1.0, 1.0)
        motor_right.throttle = constrain(speed + steering, -1.0, 1.0)

    # Control task servo with right trigger / shoulder button
    if gizmo.buttons.left_trigger:
        servo_box_stacker.angle = 90
        time.sleep(0.02)
        servo_box_stacker.angle = 0

    # Control _ with left trigger / shoulder button
    #if gizmo.buttons.right_trigger:
    #    print("LT")
    #elif gizmo.buttons.right_shoulder:
    #

    if gizmo.buttons.a:
        print("A")
        motor_arm_base.throttle = 1.0
        time.sleep(0.02)
        motor_arm_base.throttle = 0.0
        time.sleep(0.5)

    if gizmo.buttons.b:
        print("B")
        motor_arm_base.throttle = -1.0
        time.sleep(0.02)
        motor_arm_base.throttle = 0.0
        time.sleep(0.5)

    if gizmo.buttons.y:
        print("Y")
        motor_arm_updown.throttle = 1.0
        time.sleep(0.04)
        motor_arm_updown.throttle = 0.0
        time.sleep(0.5)

    if gizmo.buttons.x:
        print("X")
        motor_arm_updown.throttle = -1.0
        time.sleep(0.04)
        motor_arm_updown.throttle = 0.0
        time.sleep(0.5)


