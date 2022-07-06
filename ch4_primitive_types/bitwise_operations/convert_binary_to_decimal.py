def convert_binary_to_decimal(bin_num):
    bin_num = bin(bin_num)
    bin_num = bin_num[2:]
    bin_num = bin_num[::-1]
    value = 0
    for i, v in enumerate(bin_num):
        if v == "1":
            value += 2**i
    return value

print(convert_binary_to_decimal(0b1101))
print(convert_binary_to_decimal(0b10101))
print(convert_binary_to_decimal(0b100110))