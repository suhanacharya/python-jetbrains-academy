# put your python code here

first_number = float(input())
second_number = float(input())
operation = input()

ans = 0

if operation == "+":
    ans = first_number + second_number
    print(ans)
elif operation == "-":
    ans = first_number - second_number
    print(ans)
elif operation == "*":
    ans = first_number * second_number
    print(ans)
elif operation == "mod":
    if second_number != 0.0:
        ans = int(first_number) % int(second_number)
        print(ans)
    else:
        print("Division by 0!")
elif operation == "pow":
    ans = first_number ** second_number
    print(ans)
elif operation == "div":
    if second_number != 0.0:
        ans = int(first_number) // int(second_number)
        print(ans)
    else:
        print("Division by 0!")
elif operation == "/":
    if second_number != 0.0:
        ans = first_number / second_number
        print(ans)
    else:
        print("Division by 0!")
