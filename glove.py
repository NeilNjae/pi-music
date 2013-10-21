import pygame
import RPi.GPIO as gpio
import logging

logger = logging.getLogger(__name__)
loggerFileHandler = logging.FileHandler('glove.log')
loggerFileHandlerFormatter = logging.Formatter('%(asctime)s %(levelname)-8s  %(message)s')
loggerFileHandler.setFormatter(loggerFileHandlerFormatter)
logger.addHandler(loggerFileHandler)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)

gpio.setmode(gpio.BCM)
pins = [25, 24, 18, 22]
# pins = [25]

guitars = ['sounds/guitar1.wav',
           'sounds/guitar2.wav',
           'sounds/guitar3.wav',
           'sounds/guitar4.wav',
           'sounds/guitar5.wav']

pygame.mixer.init()

sounds = {}
for pin, wav in zip(pins, guitars):
    sounds[pin] = pygame.mixer.Sound(wav)

def handle_sound(pin):
    if not gpio.input(pin):
        sounds[pin].play()
        logger.info("Started playing {0}".format(pins.index(pin)))
    else:
        sounds[pin].stop()
        logger.info("Stopped playing {0}".format(pins.index(pin)))

for pin in pins:
    gpio.setup(pin, gpio.IN)
    gpio.add_event_detect(pin, gpio.BOTH, callback=handle_sound, bouncetime=200)

while True:
    pass
