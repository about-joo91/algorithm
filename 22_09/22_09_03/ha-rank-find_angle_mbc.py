import math

height = int(input())
under_line = int(input())

rad = math.atan2(height,under_line)
degree = round(rad * 180 / math.pi)
print(degree,chr(176),sep="")