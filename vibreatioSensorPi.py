
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)

# GPIO.setup(4, GPIO.IN)
# GPIO.setup(11, GPIO.OUT)
# GPIO.add_event_detect(4, GPIO.BOTH)


# def my_callback():
# 	# GPIO.output(25, GPIO.input(4))
# 	gpio_control(11,True)
# 	time.sleep(0.02)
# 	gpio_control(11,False)
# 	time.sleep(2)



# GPIO.add_event_callback(4, my_callback)







# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# def button_callback(channel):
#     print("Button was pushed!")
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
# message = input("Press enter to quit\n\n") # Run until someone presses enter
# GPIO.cleanup() # Clean up


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(11, GPIO.OUT)  #LED to GPIO24

try:
    while True:
         button_state = GPIO.input(10)
         if button_state == True:
             GPIO.output(11, True)
             print('Button Pressed...')
             time.sleep(0.2)
             GPIO.output(11, False)
             time.sleep(1)
         else:
             GPIO.output(11, False)
except:
    GPIO.cleanup()