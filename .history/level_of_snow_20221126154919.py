from typing import Iterable


terrain:Iterable[int] = [0,1,2,0,1,2,0,4,2,3,0]
expected_result:int = 8

# def find_next_peak(last_peak:int, terrain:Iterable[int]) -> int:
#     pass

last_peak:int=0

snow:int=0
actual_snow_level:int = 0

for index, point in enumerate(terrain[1:-1],start=1):
    if point == max(terrain[index-1:index+1]):
        if point > last_peak:
            actual_snow_level = point
    print(actual_snow_level)
