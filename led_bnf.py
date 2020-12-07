# Basic scrip. Lights one led after the next from a list. Direction reversed when it hit the end or beginning of the list.
# GPIO OUT // BOARD 11, 13, 15 : BCM 18, 27, 22
# GROUND // BOARD 9
# 3x 220 ohm resistor
# 3x leds
# jumper wires: male/male and male/female

from gpiozero import LED
from time import sleep


led_green = LED(22)
led_yellow = LED(27)
led_red = LED(17)

led_list = [led_green, led_yellow, led_red]

t = 0.1

direction = 1
index = 0

while True:
    if index == 2:
        led_list[index].on()
        direction = -1
        sleep(t)
        led_list[index].off()
    elif index == 0:
        led_list[index].on()
        direction = 1
        sleep(t)
        led_list[index].off()
    else:
        led_list[index].on()
        sleep(t)
        led_list[index].off()
    index = index + 1 * direction
