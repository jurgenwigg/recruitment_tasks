"""Calculate how much snow will fall in the valleys."""
from typing import Iterable

terrain: Iterable[int] = [0, 1, 2, 0, 1, 2, 0, 4, 0, 2, 3, 7, 8, 9]
expected: Iterable[int] = [0, 0, 0, 2, 1, 0, 2, 0, 4, 2, 1, 0, 0, 0]
expected_result: int = sum(expected)

# Set some default values.
last_peak: int = 0
snow: int = 0
actual_snow_level: int = 0
valley: Iterable[int] = []

for index, point in enumerate(terrain):
    # Set the default value for the first point.
    if index == 0:
        is_point_highest = point > terrain[index + 1]
    else:
        try:
            is_point_highest = point > terrain[index - 1] and point > terrain[index + 1]
        except IndexError:
            is_point_highest = point > terrain[index - 1]
    if is_point_highest:
        # Take a lower peak as a reference point.
        actual_snow_level = min([last_peak, point])
        # Set the last peak to the actual point.
        last_peak = point
        # Calculate how much snow fell in the valley.
        snow += sum(
            (
                actual_snow_level - elem
                for elem in valley
                if actual_snow_level - elem >= 0
            )
        )
        # Reset the valley list.
        valley = []
        continue
    # If the point is not a peak then add it to the valley list.
    valley.append(point)

print(f"Total number of snow in valleys: {snow}")
print(f"Expected number of snow: {expected_result}")
print(f"Check if the result is correct: {snow==expected_result}")
