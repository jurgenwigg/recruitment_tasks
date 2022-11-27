from typing import Iterable


terrain:Iterable[int] = [0,1,2,0,1,2,0,4,0,2,3,7,8,9]
expected =              [0,0,0,2,1,0,2,0,4,2,1,0,0,0]
expected_result:int = sum(expected)

last_peak:int=0
snow:int=0
actual_snow_level:int = 0
temp_terr = []

for index, point in enumerate(terrain):
    # sprawdzamy czy punkt jest szczytem
    if index == 0:
        is_point_highest = point>terrain[index+1]
    else:
        try:
            is_point_highest = point>terrain[index-1] and point>terrain[index+1]
        except IndexError:
            is_point_highest = point>terrain[index-1]
    if is_point_highest:
        # wybieramy mniejszy szczyt jako aktualny poziom sniegu
        actual_snow_level = min([last_peak, point])
        # zawsze chcemy wiedziec jak wysoki byl ostatni szczyt
        last_peak = point
        # dodajemy ilosc sniegu w dolinie wiedzac jaki jest mniejszy szczyt
        snow += sum([actual_snow_level-elem for elem in temp_terr if actual_snow_level-elem>=0])
        #zerujemy tymczasowa tablice terenu
        temp_terr=[]
        continue
    # jesli nie jest szczytem to dodaj wartosc terenu
    temp_terr.append(point)

print(snow)
print(expected_result)
print(snow==expected_result)