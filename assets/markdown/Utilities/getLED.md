# getLED function

## Overview

The `getLED` function takes two integer inputs, `input_x` and `input_y`, and returns an integer output representing the number of an LED based on the given X and Y coordinates. This function is useful for applications that require mapping LED coordinates to LED numbers.

## Function Signature

```py
def getLED(input_x: int,
           input_y: int) -> int:
    pass
```

## Parameters

- `input_x` = `(int)`: The X coordinate of the LED. This must be an integer.
- `input_y` = `(int)`: The Y coordinate of the LED. This must be an integer.

## Return Value

- `int`: The number of the LED based on the given X and Y coordinates. This is an integer value.

## Function Description

The `getLED` function takes in two integer inputs, `input_x` and `input_y`, which represent the X and Y coordinates of the LED, respectively. The function calculates the number of the LED based on these coordinates and returns it as an integer value.

The function first calculates the output variable as `input_y * board_width`. Then, based on the parity of `input_y`, the function determines whether to count from left to right or right to left on the row. If `input_y` is even,the function counts from left to right (i.e., `right_direction` is True), and if `input_y` is odd, the function counts from right to left (i.e., `right_direction` is False).

If `right_direction` is True, the function adds `input_x` to the output variable. Otherwise, the function adds `((board_width - 1) - input_x)` to the output variable. Finally, the function returns the output variable plus 1 (to account for the fact that LED numbering starts at 1, not 0).

## Example Usage

```py
# Set the board width
board_width = 8

# Get the LED number for X=2, Y=3
led_number = getLED(2, 3)

print(led_number)  # Output: 22
```

In the example above, we set the `board_width` variable to 8 and call the `getLED` function with `input_x` equal to 2 and `input_y` equal to 3. The function returns the number of the LED at those coordinates, which is 22. We then print the value of `led_number`, which outputs `22`.

## Exceptions

- `TypeError`: If either `input_x` or `input_y` is not an integer, a `TypeError` is raised.

## Notes

- This function assumes that the `board_width` variable has been set to the correct valuefor the board being used. If `board_width` is not set or is set incorrectly, the function may return an incorrect LED number.

- This function assumes that the LED numbering starts at 1 and not 0. If the LED numbering starts at a different value, the function should be modified accordingly.

- The `getLED` function does not perform any error checking on the input values beyond checking that they are integers. It is the responsibility of the calling code to ensure that the input values are within the appropriate range for the LED board being used.

- The coordinate system starts from the bottom left and the first LED is at position $(0, 0)$.