# read animals.txt
# and write animals_new.txt
old = open("animals.txt", "r")
new = open("animals_new.txt", "w")

old_animals = old.read()
old_animals = old_animals.split("\n")

for animal in old_animals:
    if animal != '':
        new.write(animal + " ")

old.close()
new.close()
