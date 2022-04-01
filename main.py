from machine import Pin
import time

switch1 = Pin(28, Pin.IN)
switch2 = Pin(27, Pin.IN)
led1 = Pin(1, Pin.OUT)
led2  = Pin(2, Pin.OUT)

while 1:
  if switch1.value() == 1:  
    led1.on()
  else:
    led1.off()

  if switch2.value() == 1 and led2.value() == 0:
    led2.on()
    time.sleep_ms(1000)
 
  elif switch2.value() == 1 and led2.value() == 1:
    led2.off()
    time.sleep_ms(1000)
