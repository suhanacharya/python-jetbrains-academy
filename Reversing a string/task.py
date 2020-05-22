n = int(input())

string = []

for x in range(n):
    string.append(input())

my_stack = []

for x in range(n):
    my_stack.append(string.pop())

for x in my_stack:
    print(x)