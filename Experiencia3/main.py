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

#Guía de programación
#¿Puedes programar el ShooterBot para escanear la sala y detectar objetos? Si un objeto está más cerca de 40 cm, el ShooterBot debe hacer brillar una luz de advertencia y luego disparar si el objeto no se aleja.

#Guía de testeo
#Coloque el ShooterBot en el medio de la plataforma de prueba y ejecute el programa.

#ShooterBot debe dar vuelta en un círculo mientras brilla la luz verde.

#Cuando un objeto está a menos de 40 cm de distancia, el ShooterBot se detiene, cambia la lámpara de verde a azul y luego reproduce un sonido de advertencia. Para emitir un tono debe usar la función PlayTone().

#Si el objeto aún no se ha movido, el ShooterBot dispara una bola y continúa disparando cada 2 segundos hasta que el objeto esté fuera del alcance.

#Vea si el ShooterBot:
#Se detiene, reproduce un sonido de advertencia y luego cambia el color de la lámpara cuando los objetos se encuentran a menos de 40 cm. Si no, verifique las propiedades del sensor ultrasónico.
#Cambia la lámpara de azul a rojo después de 3 segundos y hace sonar una alarma. De lo contrario, verifique que su sensor ultrasónico esté configurado para detectar un objeto a menos de 40 cm.



# Create your objects here.
ev3 = EV3Brick()


motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S4)


while True:
    
    motor_b.run(200)
    motor_c.stop()
    ev3.light.on(Color.GREEN)

    
    if ultrasonic_sensor.distance() < 200:
       
        motor_b.stop()
        motor_c.stop()
        ev3.light.on(Color.YELLOW)

        while (ultrasonic_sensor.distance() <= 200  ):
            wait(2000)
            ev3.speaker.play_file(SoundFile.LASER)
        ev3.light.on(Color.GREEN)

    


