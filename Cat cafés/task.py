cafe_names = []
no_of_cats = []

cafe = {}

while True:
    cafe_and_cats = input()
    if cafe_and_cats == "MEOW":
        break
    cafe_and_cats = cafe_and_cats.split(" ")
    cafe[int(cafe_and_cats[1])] = cafe_and_cats[0]

print(cafe[max(cafe.keys())])
