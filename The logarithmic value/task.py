import math
value = int(input())
base = int(input())

if base <= 0:
    log = round(math.log(value, math.e), 2)
else:
    log = round(math.log(value, base), 2)

print(log)
