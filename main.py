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

ucom = 0
result = compass.read(reg = 0x42, length = 1)
alpha = int(result[0]) * 2
stage = 1
col = False
sens = sensors.sensor()
while True:
    sens.read()
    amb, compas, dir, see = sens.read() 
    if amb>25 and see > 120 :
        col = True
        ev3.speaker.beep()
    else:
        col=False
   
  
    err = alpha - compas
    er = err / 180
   
    if stage == 1:
        
        u = (dir - 5) * ks
    
    
        if dir == 5 and see  > 120 and col ==True:
            ev3.speaker.beep()
            stage = 2
    #if err > 100:
       # while err > 90:
        #    motorb.dc(60)
        #   motorc.dc(45)
    
    elif stage == 2:
        
        u = ucom
        
        if er > 0:
            er = math.floor(er)
        else:
            er = math.ceil(er)
        ucom = kc*(err - er*360)
        
            
        if abs(ucom)>20:
            if ucom>0:
                ucom=20
            else:
                ucom = -20
        if dir != 5 and see  < 120:
                stage = 1
                ev3.speaker.beep()
        
        
        if stage == 3:
            motora.dc(100)
            if dir == 5 and see  > 120 and col ==True:
                ev3.speaker.beep()
                
                stage = 2

            if dir != 5 and see  < 120:
                
                stage = 1
                ev3.speaker.beep()
                
                

    
    motorb.dc(v+u)
    motorc.dc(v-u)
    ev3.screen.clear()
    ev3.screen.print(dir)
    ev3.screen.print(see)
    ev3.screen.print(timer_dlya_pinalki)
    ev3.screen.print(stage)
    wait(10)  


