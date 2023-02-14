from m5stack import *
from m5ui import *
from uiflow import *
import machine
from easyIO import *
import time


setScreenColor(0x111111)


duration = None



label0 = M5TextBox(103, 7, "label0", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=90)

from numbers import Number



def buttonA_wasReleased():
  global duration, PWM0
  PWM0.pause()
  digitalWrite(26, 1)
  wait_ms(duration)
  digitalWrite(26, 0)
  pass
btnA.wasReleased(buttonA_wasReleased)

def buttonB_wasReleased():
  global duration, PWM0
  duration = (duration if isinstance(duration, Number) else 0) + 10
  if duration >= 150:
    duration = 0
  label0.setText(str(duration))
  pass
btnB.wasReleased(buttonB_wasReleased)

def buttonA_pressFor():
  global duration, PWM0
  PWM0 = machine.PWM(26, freq=50, duty=12, timer=0)
  PWM0.resume()
  pass
btnA.pressFor(0.8, buttonA_pressFor)


duration = 10
label0.setText(str(duration))
PWM0 = machine.PWM(26, freq=50, duty=12, timer=0)
digitalWrite(26, 0)
