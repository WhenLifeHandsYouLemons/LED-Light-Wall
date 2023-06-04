# rainbowCycle function

```py
from rainbowio import colorwheel

def rainbowCycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbowCycle(0.1)
```

This function sets all the LEDs to a rainbow colour, it then moves through the LEDs creating a rainbow cycle. This section of code can be copy and pasted as an experiment.

This function requires the NeoPixel library.
