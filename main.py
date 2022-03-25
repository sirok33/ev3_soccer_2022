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
result = compass.read(reg = 0x42, length = 1)
alpha = int(result[0]) * 2
stage = 1
col = False
sens = sensors.sensor()
def motors(_u, _v ):
    motorb.dc(_v+_u)
    motorc.dc(_v-_u)
    return

def debug(*arg):
    ev3.screen.clear()
    for arg in args:
        ev3.screen.print(arg)
    return
while True:
    motors(u, v)
    sens.read()
    amb, compas, dir, see, az, ucom = sens.read() 
    if amb>25 and see > 120 :
        col = True
        ev3.speaker.beep()
    else:
        col=False

      
    if stage == 1:
        motora.dc(0)
        u = (dir - 5) * ks
        if az > 120 and dir ==7:
            while az > 90:
                sens.read()
                amb, compas, dir, see, az, ucom = sens.read()
                u = (dir - 7) * ks
                motorb.dc(v+u)
                motorc.dc(v-u)
                ev3.screen.clear()
                ev3.screen.print(dir)
                ev3.screen.print(az)
                ev3.screen.print(see)
                ev3.screen.print(stage)
                ev3.screen.print(kick_time)
                wait(10)
        else:
            stage = 1
                
        if az > 120 and dir ==3:
            while az >90:
                sens.read()
                amb, compas, dir, see, az, ucom = sens.read()
                u = (dir - 3) * ks
                motorb.dc(v+u)
                motorc.dc(v-u)
                ev3.screen.clear()
                ev3.screen.print(dir)
                ev3.screen.print(az)
                ev3.screen.print(see)
                ev3.screen.print(stage)
                ev3.screen.print(kick_time)
                wait(10)
        else:
            stage = 1



    
        if dir == 5 and see  > 120 and col ==True:
            ev3.speaker.beep()
            stage = 2
            start_time = time.time()
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
        #ucom = kc*(err - er*360)
        if time.time() - start_time > 1:
            start_time = time.time()
            while time.time() - start_time < 0.1:
                sens.read()
                motora.dc(100)
            if dir != 5 and see  < 120:
                stage = 1
                ev3.speaker.beep()


        if abs(ucom)>20:
            if ucom>0:
                ucom=20
            else:
                ucom = -20
        
        if dir != 5 and see  < 120:
                stage = 1
                start_time = 0
                ev3.speaker.beep()
       
    motorb.dc(v+u)
    motorc.dc(v-u)
    ev3.screen.clear()
    ev3.screen.print(dir)
    ev3.screen.print(az)
    ev3.screen.print(see)
    ev3.screen.print(stage)
    ev3.screen.print(kick_time)
    wait(10)
                

    


