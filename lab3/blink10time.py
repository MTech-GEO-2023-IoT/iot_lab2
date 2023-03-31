#Python Program to demonstrate GPIO Output in Raspberry Pi
#(C)Sai Shibu
#Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BCM) 
#Configure GPIO Pin 17 as output
GPIO.setup(17,GPIO.OUT) 

#Blink the LED 5 times
a=10
while a!=0:
    #Set GPIO Pin to High
    GPIO.output(17,GPIO.HIGH)
    #Wait for 1sec
    time.sleep(1)
    #Set GPIO Pin to Low
    GPIO.output(17,GPIO.LOW)
    #Wait for 1sec
    time.sleep(1)
    a=a-1
    time.sleep

#Cleanup GPIO
GPIO.cleanup()
