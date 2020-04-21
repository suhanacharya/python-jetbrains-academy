numbers = [int(x) for x in input().split()]

mean = 0

for number in numbers:
    mean += number

print(mean / len(numbers))
