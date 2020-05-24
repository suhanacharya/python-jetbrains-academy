import itertools

for x in range(1, 4):
    my_iter = itertools.combinations(flower_names, x)
    for item in my_iter:
        print(item)
