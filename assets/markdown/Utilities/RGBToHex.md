# RGBToHex function

## Overview

The `RGBToHex` function takes a tuple of three integers representing an RGB color, and returns the corresponding hexadecimal value of that color as a string. This function is useful for applications that require converting RGB colors to hexadecimal format.

## Function Signature

```py
def RGBToHex(colour: Tuple[int, int, int]) -> str:
    pass
```

## Parameters

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color. The first integer represents the red component, the second integer represents the green component, and the third integer represents the blue component. Each component must be an integer between 0 and 255, inclusive.

## Return Value

- `(str)`: A string representing the hexadecimal value of the input RGB color.

## Function Description

The `RGBToHex` function takes a tuple of three integers, `colour`, which represents an RGB color. The function converts the RGB color to its corresponding hexadecimal value and returns it as a string.

The function first formats the `colour` tuple as a string in the format `"{:02x}{:02x}{:02x}"`, where each `{:02x}` represents the hexadecimal value of one of the color components, zero-paddedto two digits. The function then uses the `int()` function to convert the formatted string to an integer value using a base of 16, which represents the hexadecimal number system.

Finally, the function returns the converted integer value as a string, which is the hexadecimal representation of the input RGB color.

## Example Usage

```py
# Convert (255, 0, 0) to hexadecimal
hex_value = RGBToHex((255, 0, 0))

print(hex_value)  # Output: "ff0000"
```

In the example above, we call the `RGBToHex` function with the tuple `(255, 0, 0)`, which represents the RGB color red. The function returns the corresponding hexadecimal value of the color as a string, which is `"ff0000"`. We then print the value of `hex_value`, which outputs `"ff0000"`.

## Exceptions

- `TypeError`: If the `colour` parameter is not a tuple of three integers, a `TypeError` is raised.

- `ValueError`: If any of the color components in the `colour` tuple is not an integer between 0 and 255, inclusive, a `ValueError` is raised.

## Notes

- The `RGBToHex` function assumes that the input color is in the RGB color space, where the red, green, and blue color components are each represented as an integer between 0 and 255, inclusive. If the input color is in a different color space, such as HSL or CMYK, the function should be modified accordingly.

- The `RGBToHex` function does not perform any error checking beyond checking that the `colour` parameter is a tuple of three integers. It is the responsibility of the calling code to ensure that the input color is valid and within the appropriate range for the RGB color space.