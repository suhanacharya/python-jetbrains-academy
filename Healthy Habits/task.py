# the list "walks" is already defined
# your code here
s = 0

for day in walks:
    s += day.get("distance")

mean = round(s / 7)

print(mean)
