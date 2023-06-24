# randomiseImage function

## Overview

The `randomiseImage` function cycles through random images from a directory and displays them on the screen. The function chooses a random image from the directory, displays it on the screen, and then waits for a specified amount of time. The function repeats this process until all images in the directory have been displayed.

## Function Signature

```py
def randomiseImage(delay: float = 0.0) -> None:
    pass
```

## Parameters

- `delay` = `float`: A float value representing the time to wait between each image being displayed on the screen. The default value is 0 seconds.

## Return Value

- `None`: The function does not return any value.

## Function Description

The `randomiseImage` function cycles through random images from a directory and displays them on the screen.

The function starts by getting the file paths of all images in the given directory using the `os.listdir` function. It then creates a list of all the image paths by concatenating the directory path with the image file name.

The function then enters a loop where it chooses a random number between 0 and the total number of images in the directory minus 1 using the `random.randint` function. If the chosen number has not already been chosen before, the function displays the corresponding image on the screen using the `displayImage` function, adds the chosen number to an array of chosen numbers, and waits for a specified amount of time using the `time.sleep` function.

The loop repeats until all images in the directory have been displayed on the screen.

## Example Usage

```py
# Cycle through random images with a delay of 1 second
randomiseImage(1)
```

In the example above, we call the `randomiseImage` function to cycle through random images from a directory and display them on the screen. The function waits for 1 second between each image being displayed.

## Exceptions

- The `randomiseImage` function assumes that the `os.listdir` function is defined properly and can be used to get the file paths of all images in a directory. If this function is not defined properly, the function may not work as expected.

- The `randomiseImage` function assumes that the `displayImage` and `time.sleep` functions are defined properly and can be used to display images on the screen and wait for a specified amount of time. If these functions are not defined properly, the function may not work as expected.