# num_to_colours list and COLOURS loop

## Overview

The `num_to_colours` list is a list of `int` values that represent the different colours available for the board. The loop that populates `num_to_colours` iterates through the `COLOURS` dictionary and appends the keys (i.e., the integer values) to the list.

## Definitions

- `COLOURS`: A dictionary of colour names and their corresponding RGB values. Each key's value is a tuple of three `int` values representing the red, green, and blue values of the colour.

## Variables

- `num_to_colours` = `(list[string])`: A list of `string` values representing the different colours available for the board.

## Loop Description

The `for` loop iterates through the keys of the `COLOURS` dictionary and appends each key (i.e., the string values representing the colours) to the `num_to_colours` list.

## Example Usage

```py
# Define the COLOURS dictionary
COLOURS = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Magenta": (255, 0, 255),
    "Cyan": (0, 255, 255),
    "White": (255, 255, 255)
}

# Create the num_to_colours list
num_to_colours = []
for key in iter(COLOURS):
    num_to_colours.append(key)

print(num_to_colours)  # Output: ["Red", "Green", "Blue", "Yellow", "Magenta", "Cyan", "White"]
```

In the example above, we define the `COLOURS` dictionary with seven colours, each represented by a different `string` value. We then create the `num_to_colours` list using the `for` loop described above. Finally, we print the value of `num_to_colours`, which outputs `["Red", "Green", "Blue", "Yellow", "Magenta", "Cyan", "White"]`.

## Notes

- The `COLOURS` dictionary must be defined before the `num_to_colours` list is created, or the loop will not be able to access the keys of the dictionary.

- The `num_to_colours` list can be used to map integer values to their corresponding colours in the `COLOURS` dictionary.