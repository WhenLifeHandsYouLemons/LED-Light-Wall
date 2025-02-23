# displayImage function

## Overview

The `displayImage` function displays an image on the screen. The function loads an image from a given file path, resizes it to fit the screen dimensions, and displays it on the screen. The function can also blend the image with the existing screen contents and lock the aspect ratio of the image.

## Function Signature

```py
def displayImage(pixel_framebuf,
                 image_path: str,
                 blend: bool = False,
                 lock_aspect: bool = False) -> None:
    pass
```

## Parameters

- `pixel_framebuf`: A Neopixel pixel_framebuffer object to display the text and images on.

- `image_path` = `str`: A string representing the file path of the image to be displayed.

- `blend` = `bool`: A boolean value representing whether to blend the image with the existing screen contents. The default value is `False`.

- `lock_aspect` = `bool`: A boolean value representing whether to lock the aspect ratio of the image. If `True`, the image will be resized to fit the width of the screen while maintaining its aspect ratio. If `False`, the image will be resized to fit the screen dimensions. The default value is `False`.

## Return Value

- `None`: The function does not return any value.

## Function Description

The `displayImage` function displays an image on the screen.

The function starts by loading the image from the given file path using the `Image.open` function from the `Pillow` library. If the `lock_aspect` parameter is set to `True`, the function resizes the image to fit the width of the screen while maintaining its aspect ratio using the `thumbnail` function. Otherwise, the function resizes the image to fit the screen dimensions using the `resize` function.

If the `blend` parameter is set to `True`, the function creates a new transparent image with the same dimensions as the screen using the `Image.new` function and blends the loaded image with the transparent image using the `alpha_composite` function. The blended image is then converted to RGB format and displayed on the screen using the `pixel_framebuf.image` and `pixel_framebuf.display` functions.

If the `blend` parameter is set to `False`, the loaded image is converted to RGB format and displayed on the screen using the `pixel_framebuf.image` and `pixel_framebuf.display` functions.

## Example Usage

```py
# Display an image on the screen without blending and without locking aspect ratio
displayImage(pixel_framebuf, "image.png")

# Display an image on the screen with blending and with locking aspect ratio
displayImage(pixel_framebuf, "image.png", blend=True, lock_aspect=True)
```

In the example above, we call the `displayImage` function to display an image on the screen. The first call displays the image without blending and without locking the aspect ratio. The second call displays the image with blending and with locking the aspect ratio.

## Exceptions

- The `displayImage` function assumes that the `Image.open` function from the `Pillow` library is defined properly and can be used to load images from file paths. If this function is not defined properly, the function may not work as expected.

- The `displayImage` function assumes that the `pixel_framebuf.image` and `pixel_framebuf.display` functions are defined properly and can be used to display images on the screen. If these functions are not defined properly, the function may not work as expected.

- The `displayImage` function may not work as expected if the image file path is incorrect or if the image cannot be loaded from the file path. In this case, the function may raise a `FileNotFoundError` or an `OSError`.

- The `displayImage` function may not work as expected if the loaded image cannot be resized or blended properly. In this case, the function may raise a `ValueError` or a `TypeError`.
