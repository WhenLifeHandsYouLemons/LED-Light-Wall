Using
[Bresenham's Circle Algorithm](https://en.m.wikipedia.org/wiki/Midpoint_circle_algorithm), we can compute one octant (one eighth of a circle) and then mirror it four times, flip the x and y values, and mirror it 4 more times to get the whole circle.


## Bresenham's Circle Algorithm

1. Given a radius, $r$, we can store $x=r$ and $y=0$.
2. The $y$ value will be incremented for every point, while the $x$ value will be calculated using a simple comparison.
3. The first point of the circle will be $(x, y)$. Which equates to $(r, 0)$.
4. Increment the $y$ value. Which equates to $(x, y+1)$.
5. If $x^2 + y^2 - r^2 > 0$, then the next point of the circle will be $(x-1, y)$.
6. If $x^2 + y^2 - r^2 \le 0$, then the next point of the circle will be $(x, y)$.
7. Repeating step 4 onwards until $x < y$.
8. Once all the points for the first octant has been computed, all the points should be positive $x$ and $y$ values.
9. Reflect the points in the $x$ only, $y$ only, and $x$ and $y$ axes. This gives the coordinates for three more octants.
10. Flip the $x$ and $y$ values of the originally computed points and repeat step 9 to get the last 4 octants.
11. Display all stored points on the grid, assuming $(0, 0)$ is the center of the grid.


## Implementation

This looks like a simple implementation:
[GeeksForGeeks: Mid-Point Circle Drawing Algorithm](https://www.geeksforgeeks.org/mid-point-circle-drawing-algorithm/amp/)

The explanation is simpler in this example but then starts to get more detailed, which we don't need.

Here's a live demo: [Bresenham Circle Algorithm Demo](http://0x80.pl/articles/bresenham-demo-circle.html)

It looks like it skips a few LEDs, but it would work better with a larger number of LEDs. As the animation will move quickly, you might not be able to see that it skips LEDs, and it might look more natural (more like an actual circular wave).

After getting all the coordinates, we can store it all into an array. Once the circle's coordinates are stored, we can iterate through and update all the LEDs in those positions and then do ```pixels.show()``` to update the LEDs.
