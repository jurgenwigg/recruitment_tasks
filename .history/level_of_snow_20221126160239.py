from typing import Iterable


terrain:Iterable[int] = [0,1,2,0,1,2,0,4,2,3,0]
expected_result:int = 8

last_peak:int=0
snow:int=0
actual_snow_level:int = 0

for index, point in enumerate(terrain[1:-1],start=1):
    print(point)
    print(max(terrain[index-1:index+2]))
    print(terrain[index-1:index+2])
    print('---')
    if point == max(terrain[index-1:index+1]):
        actual_snow_level = point if point<=last_peak else last_peak
        last_peak = point
        # print(actual_snow_level)
        # print(last_peak)
        # print('---')
        continue
    snow += actual_snow_level - point
print('***')
print(snow)
