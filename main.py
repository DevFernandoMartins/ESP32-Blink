#########################################################
#               Fernando Martins Ferreira               #
#########################################################
#                                                       #
# GitHub: https://github.com/DevFernandoMartins         #
# Instagram: https://instagram.com/devfernandomartins   #
#                                                       #
#########################################################

import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
tempo = 0.8

while True:
    led.on()
    time.sleep(tempo)
    led.off()
    time.sleep(tempo)