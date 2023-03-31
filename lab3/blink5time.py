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
for i in range(5):
    #Set GPIO Pin to High
    GPIO.output(17,GPIO.HIGH)
    #Wait for 1sec
    time.sleep(1)
    #Set GPIO Pin to Low
    GPIO.output(17,GPIO.LOW)
    #Wait for 1sec
    time.sleep(1)

#Cleanup GPIO
GPIO.cleanup()
