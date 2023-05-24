# LED Light Board

## General Information

Write something about this project here. I don't know what to write.

## Documentation

### NeoPixel

```python
pixel_pin = board.D18
```

The `pixel_pin` corresponds to the pin that the data pin of the LEDs are connected to the RPi board. This requires `import board`.

```python
pixel_brightness = 0.5
```

The brightness of the LEDs can be set as a value between 0 and 1 inclusive.

```python
pixels = neopixel.NeoPixel(board_pin, no_pixels, brightness, auto_write, pixel_order)
```

The `board_pin` function tells the computer which pin the data pin of the LEDs are connected to on the RPi board. (See _`pixel_pin`_)

`num_pixels` is the total number of LEDs that are connected. It takes a value of 0 or more.

`brightness` is the brightness of the LEDs (See _`pixel_brightness`_)

`auto_write` tells the computer whether the LEDs should change when their colour is changed (True) or whether `pixels.show()` should be run (False).

`pixel_order` tells the computer the format of the colour is going to be inputted. The accepted values could be:

* `neopixel.RGB` (most used)
* `neopixel.GRB`
* `neopixel.RGBW`

This requires `import neopixel`.

### `array()` Function

```python
new_array = array(x, y)
```

The array function creates an `x` by `y` array with all the values set to None. It returns an array which can be saved into a variable for reuse.

### `getLed()` Function

```python
max_x = 0
max_y = 0
getLed(x, y)
```

The getLed function receives a positive `x` and `y` coordinate and returns a 0 or higher which can be used to get the exact number of the LED at the coordinate, `(x, y)`.

The values `max_x` and `max_y` are the maximum x and y coordinates possible on the board.

### `transition_colors()` Function

```python
transition_colors(initial_r, initial_g, initial_b, ending_r, ending_g, ending_b, pixel_index, wait_time)
```

The transition_colors function changes the specified LEDs from one colour to another.

The `initial_r`, `initial_g`, and `initial_b` values are the initial RGB values that the LEDs will start on. The `ending_r`, `ending_g`, and `ending_b` values are the final RGB values that LEDs will show at the end. All of these should be integers between 0 and 255 inclusive.

The `pixel_index` is an integer that specifies which LED goes through the colour transition. This integer can be found using `getLed()` (See _`getLed()` Function_).

The `wait_time` is a positive float which takes the number of <b>seconds</b> that the program will wait between each change of colour. This requires `import time`.

This function requires the `set_pixels_color()` to be implemented. (See _`set_pixels_color()` Function_)

### `set_all_pixels_color()` Function

```python
set_all_pixels_color(color)
```

This function takes a colour in the format, `(r, g, b)` where `r`, `g`, and `b` are integers between 0 and 255 inclusive.

This function requires the NeoPixel library to have been initialised already (See _NeoPixels_ section).

### `set_pixels_color()` Function

```python
set_pixels_color(color, pixel_index_start, pixel_index_end=None)
```

This function takes a colour in the format, `(r, g, b)` where `r`, `g`, and `b` are integers between 0 and 255 inclusive.

The `pixel_index_start` is a positive integer which takes the first LED that you want to change the colour of. This integer can be found using `getLed()` (See _`getLed()` Function_).

The `pixel_index_end` is set to None as default. This means that only one LED will change colour. If the pixel_index_end is set to a number, the function will change all colours from `pixel_index_start` to `pixel_index_end` inclusive. This integer must be larger than `pixel_index_start`. It can be found using `getLed()` (See _`getLed()` Function_).

This function requires the NeoPixel library to have been initialised already (See _NeoPixels_ section).

### `wave()` Function

```python
wave(start_x, start_y, wave_r, wave_g, wave_b, strength, fade, time)
```

The numbers `start_x` and `start_y` are positive integers which will tell the computer the index at which the wave will start. These take a positive integer including 0.

The `wave_r`, `wave_g`, and `wave_b` take positive integers from 0 to 255 inclusive. These values are the RGB values that the wave will start on. As the wave goes on, the final colour of the LEDs will be `(0, 0, 0)`

The `strength` is how long the wave will be visible for. This takes a positive integer.

The `fade` is how long the "trail" of the wave will be. This takes a positive integer.

The `time` is the time that the computer waits before continuing after every update of the wave. This takes a positive float. This requires `import time`.

This function requires the `getLed()` function to be implementd (See _`getLed()` Function_).

### `startup()` Function

```python
startup()
```

The `startup` function doesn't take any arguments. It runs through some basic colours to check that everything is working as intended.

This function requires the NeoPixel library to have been initialised already (See _NeoPixels_ section).

It requires the `set_all_pixels_color()` to be implemented. (See _`set_all_pixels_color()` Function_)

It also requires `import time`.

In addition, it requires a `colors` dictionary to be implemented manually like so:

```python
colors = {
    "Red" : (255, 0, 0),
    "Orange" : (255, 165, 0),
    "Yellow" : (255, 255, 0),
    "Green" : (0, 255, 0),
    "Blue" : (0, 0, 255),
    "Purple" : (160, 32, 240),
    "Black" : (0, 0, 0)
}
```

### `rainbow_cycle()` Function

```python
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

```python
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