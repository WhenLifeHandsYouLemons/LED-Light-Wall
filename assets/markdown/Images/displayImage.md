# displayImage function

## Overview

The `displayImage` function displays an image on a pixel frame buffer. The function outputs the image on the pixel frame buffer.

## Function Signature

```python
def displayImage(image_path: str,
                 blend: bool = False) -> None:
    pass
```

## Parameters

- `image_path` = `(str)`: A string representing the file path of the image to be displayed on the pixel frame buffer.

- `blend` = `(bool)`: An optional boolean value indicating whether or not to blend the image with the existing pixels on the pixel frame buffer. The default value is `False`.

## Return Value

- None

## Function Description

The `displayImage` function displays an image on a pixel frame buffer using the `image` function from the `pixel_framebuf` library. The function takes in the file path of the image to be displayed on the pixel frame buffer and a boolean value indicating whether or not to blend the image with the existing pixels on the pixel frame buffer.

If the `blend` parameter is `True`, the function creates a new RGBA image with the same dimensions as the pixel frame buffer, blends the specified image with the new image using the `alpha_composite` function from the Python Imaging Library (PIL), and displays the blended image on the pixel frame buffer using the `image` function.

If the `blend` parameter is `False`, the function displays the specified image on the pixel frame buffer using the `image` function.

Finally, the function calls the `display` function from the `pixel_framebuf` library to update the pixel frame buffer with the newly displayed image.

## Example Usage

```py
# Display an image located at "/path/to/image.jpg" on the pixel frame buffer
displayImage("/path/to/image.jpg")
```

In the example above, we call the `displayImage` function to display an image located at "/path/to/image.jpg" on the pixel frame buffer.

```py
# Blend an image located at "/path/to/image.png" with the existing pixels on the pixel frame buffer
displayImage("/path/to/image.png", blend=True)
```

In the example above, we call the `displayImage` function to blend an image located at "`/path/to/image.png`" with the existing pixels on the pixel frame buffer.

## Exceptions

- The `displayImage` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `board_width` and a height of `board_height`. If the pixel frame buffer is represented differently, the `displayImage` function should be modified accordingly.

- The `displayImage` function assumes that the specified image has the same dimensions (width and height) as the pixel frame buffer. If the image has different dimensions, the `displayImage` function may not work properly and the `displayImage` function should be modified accordingly.

- The `displayImage` function assumes that the `image` and `display` functions are defined properly in the `pixel_framebuf` library. If either of these functions is not defined properly, the `displayImage` function should be modified accordingly.
