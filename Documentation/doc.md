# LED Light Board

## Documentation

### NeoPixel

```py
pixel_pin = board.D18
```

The `pixel_pin` corresponds to the pin that the data pin of the LEDs are connected to the RPi board. This requires `import board`.

```py
pixel_brightness = 0.5
```

The brightness of the LEDs can be set as a value between 0 and 1 inclusive.

```py
pixels = neopixel.NeoPixel(board_pin, no_pixels, brightness, auto_write, pixel_order)
```

The `board_pin` function tells the computer which pin the data pin of the LEDs are connected to on the RPi board. (See _`pixel_pin`_)

`num_pixels` is the total number of LEDs that are connected. It takes a value of 0 or more.

`brightness` is the brightness of the LEDs (See _`pixel_brightness`_)

`auto_write` tells the computer whether the LEDs should change when their colour is changed (True) or whether `pixels.show()` should be run (False).

`pixel_order` tells the computer the format of the colour is going to be inputted. The accepted values could be:

* `neopixel.RGB`
* `neopixel.GRB`
* `neopixel.RGBW`

This requires `import neopixel`.

### `rainbow_cycle()` Function

```py
from rainbowio import colorwheel

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbow_cycle(0.1)
```

This function sets all the LEDs to a rainbow colour, it then moves through the LEDs creating a rainbow cycle. This section of code can be copy and pasted as an experiment.

This function requires the NeoPixel library to have been initialised already (See _NeoPixels_ section).

### `randomiser()` Function

```py
import time, random

def randomiser(wait):
    pixels[random.randint(0, num_pixels-1)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pixels.show()
    time.sleep(wait)

while True:
    randomiser(0.1)
```

This function sets a random LED to a random colour. This section of code can be copy and pasted as an experiment.

This function requires the NeoPixel library to have been initialised already (See _NeoPixels_ section).
