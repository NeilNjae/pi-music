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

pygame.mixer.init()
sounds = [pygame.mixer.Sound(g) for g in guitars]
#for s in sounds:
#    s.play()
#    time.sleep(0.5)

#time.sleep(2)

gpio.setmode(gpio.BCM)
gpio.setup(25, gpio.IN)

last_switch = gpio.LOW

while True:
    this_switch = gpio.input(25)
    logger.debug("This: {0}, Last: {1}".format(this_switch, last_switch))
    if this_switch and not last_switch:
        sounds[0].play()
        last_switch = this_switch
        logger.info("Started playing")
    if not this_switch and last_switch:
        sounds[0].stop()
        last_switch = this_switch
        logger.info("Stopped playing")
