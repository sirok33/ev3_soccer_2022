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
# Create your objects here.
ev3 = EV3Brick()
compass = I2CDevice(Port.S1, 0x01)
seeker = Ev3devSensor(Port.S2)
motorb = Motor(Port.B)
motorc = Motor(Port.C)
motora = Motor(Port.A)
time1 = time.time()
color1 = ColorSensor(Port.S3)
class sensor():
    def read(self):
        amb = color1.ambient()
        result = compass.read(reg = 0x42, length = 1)
        sek_res = seeker.read("AC-ALL")
        dir = sek_res[0]
        see = 0
        see = sek_res[1]+sek_res[2]+sek_res[3]+sek_res[4]+sek_res[5]
        compas = int(result[0]) * 2  
        return amb, compas, dir, see
        
