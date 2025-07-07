#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor_b= Motor(Port.B)
motor_c=Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S4)
 

while True:
    motor_b.run(300)
    motor_c.run(300)
    if ultrasonic_sensor.distance() <= 200:
        motor_b.stop()
        motor_c.stop()
        ev3.speaker.play_file(SoundFile.LASER)
        motor_b.run(300)
        wait(2000)



 

    


 




# Write your program here.
ev3.speaker.beep()
