def tallest_people(**people):
    maxheight = max(people.values())
    for key, value in sorted(people.items()):
        if value == maxheight:
            print(f'{key} : {value}')
