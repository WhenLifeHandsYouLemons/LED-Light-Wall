# randomiseText function

## Overview

The `randomiseText` function cycles randomly through a list of preset phrases and scrolls them on the screen one by one. The function chooses a phrase at random, scrolls it on the screen, and waits for a specified amount of time before choosing another random phrase.

## Function Signature

```py
def randomiseText(pixel_framebuf,
                  colour: Tuple[int, int, int],
                  scroll_delay: float) -> None:
    pass
```

## Parameters

- `pixel_framebuf`: A Neopixel pixel_framebuffer object to display the text and images on.

- `colour` = `Tuple[int, int, int]`: A tuple of three integers representing the RGB color values for the text.

- `scroll_delay` = `float`: A float value representing the time to wait between each frame of the scrolling animation.

## Return Value

- `None`: The function does not return any value.

## Function Description

The `randomiseText` function cycles randomly through a list of preset phrases and scrolls them on the screen one by one.

The function starts by defining an array called `all_text` that contains all the preset phrases to be randomly displayed. The function also defines an empty array called `chosen_numbers` to keep track of the phrases that have already been displayed.

The function then enters a loop that continues until all the phrases in `all_text` have been displayed. In each iteration of the loop, the function chooses a random number between 0 and the number of phrases in `all_text`. If the number has not already been chosen, the function calculates the `end_x` position for the current phrase and calls the `scrollText` function to animate the phrase scrolling on the screen. The function then adds the chosen number to the `chosen_numbers` array and waits for a specified amount of time using the `time.sleep` function.

The loop continues until all the phrases in `all_text` have been displayed.

## Example Usage

```py
# Scroll through preset phrases randomly with a delay of 2 seconds between each phrase and 0.1 seconds between each frame of the scrolling animation
randomiseText(pixel_framebuf, (255, 255, 255), 0.1)
```

In the example above, we call the `randomiseText` function to cycle randomly through a list of preset phrases and scroll them on the screen.

## Exceptions

- The `randomiseText` function assumes that the `scrollText` function is defined properly and can be used to animate scrolling text on the screen. If this function is not defined properly, the function may not work as expected.

- The `randomiseText` function assumes that the `time.sleep` function is defined properly and can be used to wait for a specified amount of time. If this function is not defined properly, the function may not work as expected.

- The `randomiseText` function assumes that the `colour` parameter is a tuple of three integers representing RGB color values. If the `colour` parameter is not a tuple of three integers, the function may not work as expected.

- The `randomiseText` function assumes that the `delay` parameter is a float value representing the time to wait between each phrase. If the `delay` parameter is not a float value, the function may not work as expected.

- The `randomiseText` function assumes that the `scroll_delay` parameter is a float value representing the time to wait between each frame of the scrolling animation. If the `scroll_delay` parameter is not a float value, the function may not work as expected.

- The `randomiseText` function may not work as expected if the preset phrases in `all_text` are not defined properly or if the phrases are too large to fit on the screen. In this case, the text may be cut off or may not be visible.
