# put your python code here
stack = []
expression = list(input())
for literal in expression:

    #     if literal == ")" and len(stack) != 1:
    #         while stack[-1] != "(":
    #             stack.pop()
    #         stack.pop()
    #     else:
    #         stack.append(literal)
    #
    # if "(" not in stack and ")" not in stack:
    #     print("OK")
    # else:
    #     print("ERROR")

    if literal == ")":
        if "(" in stack:
            while "(" != stack[-1]:
                stack.pop()
            stack.pop()
        else:
            stack.append(literal)
            break
    else:
        stack.append(literal)
if "(" not in stack and ")" not in stack:
    print("OK")
else:
    print("ERROR")
