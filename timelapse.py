#!/usr/bin/env python3

import sys
import datetime
from blinkt import set_pixel, show, set_brightness
from picamera import PiCamera
from os import system
from time import sleep

if len(sys.argv) < 3:
    print('ERROR: missing argument')
    sys.exit(2)

camera = PiCamera()
#camera.resolution = (1024, 768)

# set global blinkt brightness low
set_brightness(0.05)

def blinkt_clear():
    for led in range(8):
        set_pixel(led,0,0,0)
    show()

while True:
    blinkt_clear()

    # prepare filename from given path and current time
    now = datetime.datetime.now()
    filename = sys.argv[2] + '/' + now.strftime("timelapse_%Y-%m-%d_%H-%M-%S.jpg")

    # take picture
    set_pixel(0,255,0,0)
    show()
    camera.capture(filename)
    set_pixel(0,0,0,0)
    show()

    # wait a moment
    sleep_step = int(sys.argv[1]) / 8
    for led in range(8):
        set_pixel(led,255,255,255)
        show()
        sleep(sleep_step)
        set_pixel(led,0,0,0)
        show()

