# COLOUR_MATCHES List

## Overview

The `COLOUR_MATCHES` list is a collection of lists representing sets of color matches. Each inner list contains strings representing the names of the colors that are considered matches.

## List Structure

The `COLOUR_MATCHES` list has the following structure:

```py
COLOUR_MATCHES = [
    ["Colour name 1", "Colour name 2", "Colour name 3"],
    ["Colour name 4", "Colour name 5", "Colour name 6"],
    # more sets of color matches can be added here
]
```

Each item in the array has an array of colour names that would work well together on the display.

## List Usage

The `COLOUR_MATCHES` list can be used to check if a given set of colors matches any of the sets of color matches in the list.

To check if a set of colors matches any of the sets of color matches in the `COLOUR_MATCHES` list, you can use the following code:

```py
if ["Colour name 1", "Colour name 2", "Colour name 3"] in COLOUR_MATCHES:
    # the set of colors matches the first set of color matches in COLOUR_MATCHES
    # do something here
else:
    # the set of colors does not match any of the sets of color matches in COLOUR_MATCHES
    # do something else here
```

In this example, the code checks if the set of colors "Colour name 1", "Colour name 2", and "Colour name 3" matches the set of colors in the first inner list of `COLOUR_MATCHES`.

## Notes

- The `COLOUR_MATCHES` list can contain any number of inner lists representing sets of color matches.

- The strings representing the color names in the inner lists of `COLOUR_MATCHES` must exactly match the strings used as keys in the `COLOURS` dictionary. The keys are case-sensitive.

- The order of the strings in the inner lists of `COLOUR_MATCHES` does not matter. Two sets of colors with the same color names in different orders will still be considered a match.