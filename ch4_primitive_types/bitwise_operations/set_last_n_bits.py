def set_last_n_bits(m, n):
    bit_arr_len = len(bin(m)) - 3
    mask = 2**n - 1
    if n + 1 <= bit_arr_len:
        shift = (bit_arr_len - n + 1)
    else:
        shift = 0
    mask = mask << shift
    return mask | m

print(bin(set_last_n_bits(0b10001111, 3)))
print(bin(set_last_n_bits(0b10000000, 5)))
print(bin(set_last_n_bits(0b10000000, 8)))
