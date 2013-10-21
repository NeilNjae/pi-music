import pygame
import RPi.GPIO as gpio
import logging

logger = logging.getLogger(__name__)
loggerFileHandler = logging.FileHandler('keyboard.log')
loggerFileHandlerFormatter = logging.Formatter('%(asctime)s %(levelname)-8s  %(message)s')
loggerFileHandler.setFormatter(loggerFileHandlerFormatter)
logger.addHandler(loggerFileHandler)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)

gpio.setmode(gpio.BCM)
if gpio.RPI_REVISION == 1:
    pins = [22, 21, 17, 4, 25, 24, 23, 18]
else:
    pins = [22, 27, 17, 4, 25, 24, 23, 18]
# pins = [25]

notes = ['sounds/keyboard-fsharp-low.wav',
         'sounds/keyboard-g.wav',
         'sounds/keyboard-gsharp.wav',
         'sounds/keyboard-a.wav',
         'sounds/keyboard-asharp.wav',
         'sounds/keyboard-b.wav',
         'sounds/keyboard-c.wav',
         'sounds/keyboard-csharp.wav',
         'sounds/keyboard-d.wav',
         'sounds/keyboard-dsharp.wav',
         'sounds/keyboard-e.wav',
         'sounds/keyboard-f.wav',
         'sounds/keyboard-fsharp-high.wav']

notes = ['sounds/keyboard-g.wav',
         'sounds/keyboard-a.wav',
         'sounds/keyboard-b.wav',
         'sounds/keyboard-c.wav',
         'sounds/keyboard-d.wav',
         'sounds/keyboard-e.wav',
         'sounds/keyboard-f.wav',
         'sounds/keyboard-g-high.wav']


pygame.mixer.init()

sounds = {}
for pin, wav in zip(pins, notes):
    sounds[pin] = pygame.mixer.Sound(wav)

def handle_sound(pin):
    if gpio.input(pin):
        sounds[pin].play()
        logger.info("Started playing {0}".format(pins.index(pin)))
    else:
        sounds[pin].stop()
        logger.info("Stopped playing {0}".format(pins.index(pin)))

for pin in pins:
    gpio.setup(pin, gpio.IN)
    gpio.add_event_detect(pin, gpio.BOTH, callback=handle_sound, bouncetime=50)

while True:
    pass
