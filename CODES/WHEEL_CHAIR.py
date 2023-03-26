import time
import serial
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

ser = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0


while 1:
   x=ser.read()
   y=x.decode("utf-8")
##   print(y)
   if(y=='D'):
      GPIO.output(31,True)
      GPIO.output(33,False)
      GPIO.output(35,True)
      GPIO.output(37,False)
      GPIO.output(32,True)
      GPIO.output(36,False)
      GPIO.output(38,True)
      GPIO.output(40,False)
      print("right")
      
      
   elif(y=='S'):
      GPIO.output(31,False)
      GPIO.output(33,True)
      GPIO.output(35,True)
      GPIO.output(37,False)
      GPIO.output(32,False)
      GPIO.output(36,True)
      GPIO.output(38,True)
      GPIO.output(40,False)
      print("backward")
      
      
   elif(y=='W'):
      GPIO.output(33,False)
      GPIO.output(31,True)
      GPIO.output(37,True)
      GPIO.output(35,False)
      GPIO.output(36,False)
      GPIO.output(32,True)
      GPIO.output(40,True)
      GPIO.output(38,False)
      print("forward")
      
      
   elif(y=='A'):
      GPIO.output(31,False)
      GPIO.output(33,True)
      GPIO.output(35,False)
      GPIO.output(37,True)
      GPIO.output(32,False)
      GPIO.output(36,True)
      GPIO.output(38,False)
      GPIO.output(40,True)
      print("left")
      
      
   elif(y=='X'):
      GPIO.output(31,False)
      GPIO.output(33,False)
      GPIO.output(35,False)
      GPIO.output(37,False)
      GPIO.output(32,False)
      GPIO.output(36,False)
      GPIO.output(38,False)
      GPIO.output(40,False)
      print("STOP")

      
