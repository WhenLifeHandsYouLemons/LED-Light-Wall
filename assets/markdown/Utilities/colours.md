# colours dictionary

## Overview

The `colours` dictionary is a collection of key-value pairs representing common colors in the RGB color space. The keys of the dictionary are strings representing the names of the colors, and the values are tuples of three integers representing the RGB values of the colors.

## Dictionary Structure

The `colours` dictionary has the following structure:

```py
colours = {
    "Colour name" : (255, 255, 255)
}
```

## Dictionary Usage

The `colours` dictionary can be used to access RGB color values by their corresponding names. For example, to access the RGB value of the color red, you can use the following code:

```py
red_value = colours["Red"]
```

The value of `red_value` in this case would be the tuple `(255, 0, 0)`, which represents the RGB color red.

## Notes

- The `colours` dictionary is not an exhaustive list of all possible colors in the RGB color space. It is intended as a collection of common colors, and additional colors can be added as needed.

- The keys of the `colours` dictionary are case-sensitive.

- The values of the `colours` dictionary are tuples of three integers representing the RGB values of the colors. Each integer must be between 0 and 255, inclusive.
