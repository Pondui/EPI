def convert_decimal_to_binary(num):
    set_bits = get_set_bits(num)

    largest_index = 0
    for k in set_bits:
        if k > largest_index:
            largest_index = k
    
    arr = ["0"] * (largest_index + 1)
    for k in set_bits:
        arr[k] = "1"

    res = "".join(arr)
    return res

def get_set_bits(num):
    if num == 0:
        return []

    exponent = 0 
    while 2**exponent <= num:
        exponent += 1
    
    if exponent == 0:
        num = num - 2**exponent
    else:
        num = num - 2**(exponent - 1)

    set_bits = get_set_bits(num)
    set_bits.append(exponent)
    return set_bits

print(convert_decimal_to_binary(4))
print(convert_decimal_to_binary(5))
print(convert_decimal_to_binary(7))
print(convert_decimal_to_binary(100))