import pygame
import RPi.GPIO as gpio
import time
import logging

logger = logging.getLogger(__name__)
loggerFileHandler = logging.FileHandler('glove.log')
loggerFileHandlerFormatter = logging.Formatter('%(asctime)s %(levelname)-8s  %(message)s')
loggerFileHandler.setFormatter(loggerFileHandlerFormatter)
logger.addHandler(loggerFileHandler)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)


guitars = ['sounds/guitar1.wav',
           'sounds/guitar2.wav',
           'sounds/guitar3.wav',
           'sounds/guitar4.wav',
           'sounds/guitar5.wav']

pins = [25, 24, 18, 22]
pins = [25]

pygame.mixer.init()
sounds = [pygame.mixer.Sound(g) for g in guitars]

gpio.setmode(gpio.BCM)
for pin in pins:
    gpio.setup(pin, gpio.IN)

last_states = [gpio.input(p) for p in pins]
these_states = list(last_states)


def handle_sound(pin):
    if gpio.input(pin):
        sounds[pins.index(pin)].play()
        logger.info("Started playing {0}".format(pins.index(pin)))
    else:
        sounds[pins.index(pin)].stop()
        logger.info("Stopped playing {0}".format(pins.index(pin)))


for pin in pins:
    gpio.add_event_detect(pin, gpio.BOTH, callback=handle_sound, bouncetime=200)
#    gpio.add_event_detect(pin, gpio.FALLING, callback=stop_sound, bouncetime=100)

while True:
    pass

#while True:
#    these_states = [gpio.input(p) for p in pins]
#    logger.debug("These: {0}, Last: {1}".format(these_states, last_states))
#    for i in range(len(pins)):
#        if these_states[i] and not last_states[i]:
#            sounds[i].play()
#            last_states[i] = these_states[i]
#            logger.info("Started playing {0}".format(i))
#        if not these_states[i] and last_states[i]:
#            sounds[i].stop()
#            last_states[i] = these_states[i]
#            logger.info("Stopped playing {0}".format(i))
