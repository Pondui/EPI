def replace_interval_of_bits(bit_arr, subsitute_interval, i, j):
    ''' Replace an interval [i, j] in bit_arr with substitute_interval, where i < j counting from 0 from left to right '''
    mask1 = 2**i - 1
    mask2 = ~0 << j + 1
    mask3 = mask1 | mask2
    mask4 = subsitute_interval << i

    bit_arr_clear = bit_arr & mask3
    result = bit_arr_clear | mask4

    return result

print(bin(replace_interval_of_bits(0b1100101010011, 0b11111, 3, 7)))
print(bin(replace_interval_of_bits(0b1100101010011, 0b11111, 4, 8)))
