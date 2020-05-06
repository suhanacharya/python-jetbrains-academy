class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        if self.a**2 + self.b**2 == self.c**2:
            area = 0.5 * self.a * self.b
            print(area)
        else:
            print("Not right")


sides_input = input().split()

sides = [int(x) for x in sides_input]

triangle = RightTriangle(sides[0], sides[1], sides[2])
