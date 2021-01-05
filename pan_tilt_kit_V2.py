#!/usr/bin/env python
# This is a simple program to move 2 servo motors in order to
# calibrate min, max and nominal values
# Author: Oguz Yilmaz
# Free licencse, no warranty

import Adafruit_PCA9685
import readchar, time, os

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Channel no of servos fpr pan (X) and tilt (Y)
servo_X_ch = 2
servo_Y_ch = 3

# Configure pan (X) min, max and servo pulse lengths
servo_X_nom = 414         # Nominal value of servo out of 4096
servo_X_min = 180         # Min pulse length out of 4096
servo_X_max = 660         # Max pulse length out of 4096
servo_X_set = servo_X_nom # Set value of servo, at init nominal
servo_X_steps = 8         # Pan step size of servo while moving

# Configure tilt (Y) min, max and servo pulse lengths
servo_Y_nom = 470         # Nominal value of servo out of 4096
servo_Y_min = 220         # Min pulse length out of 4096
servo_Y_max = 640         # Max pulse length out of 4096
servo_Y_set = servo_Y_nom # Set value of servo, at init nominal
servo_Y_steps = 8         # Pan step size of servo while moving

def printscreen():
    os.system('clear')
    print("a/d: Move servo left and right")
    print("w/s: Move servo up and down")
    print("q:   Move servo to default position")
    print("x:   End program")
    print("============== PWM VALUE ==============")
    print('Pan (X)  PWM value: %d' %(servo_X_set))
    print('Tilt (Y) PWM value: %d' %(servo_Y_set))

print("Press a, d, w or s to start the program")

while True:
    # get key stroke / char
    char = readchar.readchar()
    
    if(char == "a"):
        if servo_X_max > servo_X_set:
            servo_X_set = servo_X_set + servo_X_steps
            pwm.set_pwm(servo_X_ch, 0, servo_X_set)
        printscreen()
        
    if(char == "d"):
        if servo_X_min < servo_X_set:
            servo_X_set = servo_X_set - servo_X_steps
            pwm.set_pwm(servo_X_ch, 0, servo_X_set)
        printscreen()

    if(char == "s"):
        if servo_Y_max > servo_Y_set:
            servo_Y_set = servo_Y_set + servo_Y_steps
            pwm.set_pwm(servo_Y_ch, 0, servo_Y_set)
        printscreen()

    if(char == "w"):
        if servo_Y_min < servo_Y_set:
            servo_Y_set = servo_Y_set - servo_Y_steps
            pwm.set_pwm(servo_Y_ch, 0, servo_Y_set)
        printscreen()        
        
    if(char == "q"):
        #servo_X_set = servo_X_nom
        #pwm.set_pwm(servo_X_ch, 0, servo_X_set)
        #printscreen()
        while(servo_X_set != servo_X_nom):
            if(servo_X_set < servo_X_nom):
                servo_X_set = servo_X_set + servo_X_steps
            if(servo_X_set > servo_X_nom):
                servo_X_set = servo_X_set - servo_X_steps
            pwm.set_pwm(servo_X_ch, 0, servo_X_set)
            time.sleep(0.05)
        while(servo_Y_set != servo_Y_nom):
            if(servo_Y_set < servo_Y_nom):
                servo_Y_set = servo_Y_set + servo_Y_steps
            if(servo_Y_set > servo_Y_nom):
                servo_Y_set = servo_Y_set - servo_Y_steps
            pwm.set_pwm(servo_Y_ch, 0, servo_Y_set)
            time.sleep(0.05)
        printscreen()

    if(char == "x"):
        servo_X_set = servo_X_nom
        pwm.set_pwm(servo_X_ch, 0, servo_X_set)
        print("====Program ended====")
        break
        
    char = ""
