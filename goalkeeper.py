#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import I2CDevice
from pybricks.iodevices import Ev3devSensor
import math
import time
import sensors
# Create your objects here.
ev3 = EV3Brick()
compass = I2CDevice(Port.S1, 0x01)
seeker = Ev3devSensor(Port.S2)
motorb = Motor(Port.B)
motorc = Motor(Port.C)
motora = Motor(Port.A)

color1 = ColorSensor(Port.S3)
# Write your program here.
ev3.speaker.beep()
kc = 1.1
ks = 15
v = 50
err = 0
dir = 0
see = 0
kick_time = 0
ucom = 0
anglc=0
anglb=0
result = compass.read(reg = 0x42, length = 1)
alpha = int(result[0]) * 2
stage = 1
col = False
sens = sensors.sensor()
# def motors(_u, _v ):
#     motorb.dc(_v+_u)
#     motorc.dc(_v-_u)
#     return

# def debug(*arg):
#     ev3.screen.clear()
#     for arg in args:
#         ev3.screen.print(arg)
#     return
# # while True:
# #     motors(u, v)
# #     sens.read()
# #     amb, compas, dir, see, az, ucom = sens.read() 
# #     if amb>25 and see > 120 :
# #         col = True
# #         ev3.speaker.beep()
# #     else:
# #         col=False

      
    if stage == 1:
        
        if see>120 and dir==5
            motorb.reset_angle(0)
            motorc.reset_angle(0)
            stage = 2
        
    
    elif stage == 2:
        anglc = motorc.angle()
        anglb = motorb.angle()
        u = (dir - 5) * ks
        
        if dir != 5 and see  < 120:
            motorb.run_angle(50,-anglb)
            motorc.run_angle(50,-anglc)
            stage = 1
            ev3.speaker.beep()
       
    motorb.dc(v+u)
    motorc.dc(v-u)
    ev3.screen.clear()
    ev3.screen.print(dir)
    ev3.screen.print(see)
    ev3.screen.print(stage)
    wait(10)