import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)



try:
    GPIO.setmode(GPIO.BOARD)
    pinTrigger = 7
    pinEcho = 11
    buzzer= 23
 
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)
    GPIO.setup(buzzer,GPIO.OUT)
    
    while True:
        GPIO.output(pinTrigger, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
 
        time.sleep(0.00001)
        GPIO.output(pinTrigger, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)
 
        while GPIO.input(pinEcho)==0:
            pulseStartTime = time.time()
        while GPIO.input(pinEcho)==1:
            pulseEndTime = time.time()
 
        pulseDuration = pulseEndTime - pulseStartTime
        distance = round(pulseDuration * 17150, 2)
 
        
        if distance > 7.00 and distance <8.00:
            print("Distance: %.2f cm" % (distance))
            print("Medium")
            for x in range(2):
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(0.3)
            
               
        elif distance > 10.00 and distance <20.00:
            print("Distance: %.2f cm" % (distance))
            print("Medium to far")
            for x in range(2):
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(0.5)
            
            
        elif distance < 6.99 and distance >2:
            print("Distance: %.2f cm" % (distance))
            print("Close")
            
            for x in range(10):
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(0.2)
            
        elif distance < 1.99:
            print("Distance: %.2f cm" % (distance))
            print("Hit")
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(buzzer,GPIO.LOW)
            
        elif distance > 20:
            print("Distance: %.2f cm" % (distance))
            print("Far")
            
        time.sleep(0.4)

finally:
    GPIO.cleanup()

