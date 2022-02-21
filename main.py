#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


import time
# Create your objects here.
ev3 = EV3Brick()
motorb = Motor(Port.B)
motorc = Motor(Port.C)
sonic = UltrasonicSensor(Port.S2)
color1 = ColorSensor(Port.S1)
color2 = ColorSensor(Port.S3)
gyrok = GyroSensor(Port.S4)

# Write your program here.

gyric = gyrok.angle()
kp = 1.2
v = 50
u = 0
err = 0
count = 0
ref1 = color1.reflection() 
ref2 = color2.reflection()
t1 = time.time()
t2 = 0
rast = sonic.distance()
stage = 0
gyrok.reset_angle(0)
wait(300)
motorb.dc(50)
motorc.dc(50)
wait(1500)

while True:
    motorb.dc(0)
    motorc.dc(0)  
    rast = sonic.distance()
    if stage == 0 and rast<150:
        
        wait(6000)
        motorb.dc(100)
        motorc.dc(100)
        wait(2000)
        motorb.dc(0)
        motorc.dc(0)
        while rast > 300:
            motorb.dc(0)
            motorc.dc(0)
        stage = 1
             
    t2 = time.time() - t1
    t1 = time.time() - t1
    ref1 = color1.reflection() 
    ref2 = color2.reflection()
    err = ref1 - ref2
    u = kp * err
    motorb.dc(v+u)
    motorc.dc(v-u)
    if ref1 < 10 and ref2 < 10 :
        count += 1
        ev3.speaker.beep()
        wait(100)
    ev3.screen.clear()
    ev3.screen.print(t2)
    ev3.screen.print(t1)
    ev3.screen.print()


    



