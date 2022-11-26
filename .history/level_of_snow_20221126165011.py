from typing import Iterable


terrain:Iterable[int] = [0,1,2,0,1,2,0,4,1,2,3,0,2]
expected =              [0,0,0,2,1,0,2,0,2,1,0,0]
expected_result:int = 8

last_peak:int=0
snow:int=0
actual_snow_level:int = 0
temp_terr = []
for index, point in enumerate(terrain[1:],start=1):
    if index==1:
        last_peak=point
    # print(point)
    # print(max(terrain[index-1:index+2]))
    # print(terrain[index-1:index+2])
    # print(actual_snow_level - point if actual_snow_level - point>=0 else 0)
    # print('---')
    if point == max(terrain[index-1:index+2]):
        actual_snow_level = min([last_peak, point])
        last_peak = point
        # print(point)
        # print(actual_snow_level)
        # print(temp_terr)
        # print('==')
        snow += sum([actual_snow_level-elem for elem in temp_terr])
        temp_terr=[]
        continue
    temp_terr.append(point)
print('***')
print(snow)
