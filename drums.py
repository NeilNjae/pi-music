import pygame
import RPi.GPIO as gpio
import logging

logger = logging.getLogger(__name__)
loggerFileHandler = logging.FileHandler('drums.log')
loggerFileHandlerFormatter = logging.Formatter('%(asctime)s %(levelname)-8s  %(message)s')
loggerFileHandler.setFormatter(loggerFileHandlerFormatter)
logger.addHandler(loggerFileHandler)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)

gpio.setmode(gpio.BCM)
pins = [25, 24, 23, 18]
# pins = [18]

drums = ['sounds/hihat.wav',
         'sounds/maracas.wav',
         'sounds/slowdrum.wav',
         'sounds/snare.wav']

pygame.mixer.init()

sounds = {}
for pin, wav in zip(pins, drums):
    sounds[pin] = pygame.mixer.Sound(wav)

def handle_sound(pin):
    sounds[pin].play()
    logger.info("Played {0}".format(pin))

for pin in pins:
    gpio.setup(pin, gpio.IN)
    gpio.add_event_detect(pin, gpio.RISING, callback=handle_sound, bouncetime=100)

while True:
    pass
