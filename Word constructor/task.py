
string_1 = input()
string_2 = input()

res = ""

for l1, l2 in zip(string_1, string_2):
    res += (l1 + l2)

print(res)
