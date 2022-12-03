from machine import Pin
from time import sleep
from _thread import start_new_thread

led = Pin("LED", Pin.OUT)

for i in range(0, 10):
    led.on()
    sleep(0.25)
    led.off()
    sleep(0.25)

button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(14, Pin.IN, Pin.PULL_DOWN)

x = 0
y = 0

def button_down():
    global x, y
    while True:
        if button1.value() == 1:
            x += 100
            led.on()
            sleep(1)
            led.off()
        if button2.value() == 1:
            y += 100
            led.on()
            sleep(1)
            led.off()

new_thread = start_new_thread(button_down, ())

while True:
     print("{}|0|{}|0|0".format(x, y))
