{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPGj6r+Fj1dTjaYA4t01aO3"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["Sample code for servos"],"metadata":{"id":"CrIvj3GrINpf"}},{"cell_type":"code","source":["import time\n","import circuitpython_gizmo\n","import pwmio\n","import adafruit_motor\n","from adafruit_motor import servo\n","\n","gizmo = circuitpython_gizmo.Gizmo()\n","\n","motor = adafruit_motor.servo.ContinuousServo(\n","    pwmio.PWMOut(gizmo.MOTOR_4, frequency=50),\n","    min_pulse=1000,\n","    max_pulse=2000\n",")\n","\n","while True:\n","    gizmo.refresh()\n","    print(\"A: %s\" % gizmo.buttons.a)\n","    if gizmo.buttons.a:\n","        motor.throttle = 1.0\n","    else:\n","        motor.throttle = 0.0\n","    time.sleep(0.1)"],"metadata":{"id":"YrTme6OnIbZ3"},"execution_count":null,"outputs":[]}]}