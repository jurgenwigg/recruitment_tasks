# Calculate how much snow will fall to valleys
This task appears in one of the coding interviews. 
The task was to write a program/function which will calculate how much snow will fall into the valleys. It was presented in this form:
```
                                        +---+
                                        |   | *   * +---+
        +---+ *   * +---+ *   * +---+ * |   +---+ * |   |
    +---+   | * +---+   | * +---+   + * |   |   +---+   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0 | 1 | 2 | 0 | 1 | 2 | 0 | 1 | 2 | 0 | 4 | 2 | 1 | 3 | 0 
```
The candidate has to figure out the rules of snow falling into valleys and up to what level.
## Proposed Algorithm
1. Set initial values
2. Enumerate the whole terrain. In each step:
 1. Check if the point is the highest.
 2. If the point is local the highest point:
 - Choose from the last highest point and the actual lower value
 - Set last_peak to the actual point
 - Sum list of elements where one element is chosen snow level subtracted with terrain level at some point.
 - Reset points of the valley.
 3. If the point is not the highest one append it to the list of points of the valley.