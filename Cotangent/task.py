import math
angle = int(input())

cot = round(math.cos(math.radians(angle)) / math.sin(math.radians(angle)), 10)
print(cot)