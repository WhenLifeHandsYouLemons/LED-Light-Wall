"""
Main loop
"""
import sys
import pygame

# Custom imports
from pygame_constants import *
from pygame_utilities import *
from pygame_precomputations import *

# Reset board
setAllPixelsColour(COLOURS["Black"])

print("\nStarting display.")

while RUNNING_WINDOW == True:
    clock.tick(60)

    print("\nCalculating waves...")
    merged, non_merged = randomisePatterns()

    print("Displaying waves.")
    displayRandomPatterns(merged, non_merged)

    setAllPixelsColour(COLOURS["Black"])

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()

sys.exit()
