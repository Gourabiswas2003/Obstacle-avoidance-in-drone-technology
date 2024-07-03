#VCC to 5V on Raspberry Pi
#GND to Ground on Raspberry Pi
#Trig to GPIO pin 23 (can be changed)
#Echo to GPIO pin 24 (can be changed)

import RPi.GPIO as GPIO
import time

# GPIO Mode (BCM)
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # Set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # Set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Save StartTime
    StartTime = time.time()
    StopTime = time.time()

    # Save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # Save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # Time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # Multiply with the sonic speed (34300 cm/s)
    # Divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if _name_ == "_main_":
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
