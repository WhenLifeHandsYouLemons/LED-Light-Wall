# randomDots function

```py
import time, random

def randomDots(delay):
    pixels[random.randint(0, num_pixels-1)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pixels.show()
    time.sleep(delay)

while True:
    randomDots(0.1)
```

This function sets a random LED to a random colour. This section of code can be copy and pasted as an experiment.

This function requires the NeoPixel library.
