
in_code = list(input())
in_key = int(input())

conv_byte = in_key.to_bytes(2, byteorder="little")

sum_bytes = sum(conv_byte)

for i in range(len(in_code)):
    in_code[i] = chr(ord(in_code[i]) + sum_bytes)

in_code = "".join(in_code)

print(in_code)
