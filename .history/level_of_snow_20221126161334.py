from typing import Iterable


terrain:Iterable[int] = [0,1,2,0,1,2,0,4,1,2,3,0]
expected =              [0,0,0,2,1,0,2,0,2,1,0,0]
expected_result:int = 8

last_peak:int=0
snow:int=0
actual_snow_level:int = 0

for index, point in enumerate(terrain[1:-1],start=1):
    print(point)
    print(max(terrain[index-1:index+2]))
    print(terrain[index-1:index+2])
    print(actual_snow_level - point if actual_snow_level - point>=0 else 0)
    print('---')
    if point == max(terrain[index-1:index+2]):
        last_peak = point
        actual_snow_level = point if point<=last_peak else last_peak
        print(actual_snow_level)
        print('==')
        # print(last_peak)
        # print('---')
        continue
    snow += actual_snow_level - point #if actual_snow_level - point>=0 else 0
print('***')
print(snow)
