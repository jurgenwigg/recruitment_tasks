# Calculate how much snow will fall to valleys
This task appears on one of coding interviews. 
The task was to write a program/function which will calculate how much snow will fall into the valleys. It was presented in this form:
```
                                        +---+
                                        |   | *   * +---+
        +---+ *   * +---+ *   * +---+ * |   +---+ * |   |
    +---+   | * +---+   | * +---+   + * |   |   +---+   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0 | 1 | 2 | 0 | 1 | 2 | 0 | 1 | 2 | 0 | 4 | 2 | 1 | 3 | 0 
```
Candidate has to figure out the rules of snow falling into valleys and up to what level.
## Proposed Algorithm
1. Set initial values
2. Enumerate over whole terrain. In each step:
    1. Check if point is the highest point.
    2. If point is local the highest point:
        - Choose from last highest point and actual one lower value
        - Set last_peak to actual point
        - Sum list of elements where one element is chosen snow level substracted with terrain level at some point.
        - Reset points of valley
    3. If point is not the highest one append it to list of points of valley.
