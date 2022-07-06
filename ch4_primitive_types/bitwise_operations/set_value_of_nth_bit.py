def set_value_of_nth_bit(m, n, val):
    mask1 = 2**n - 1
    mask2 = ~0 << n + 1
    mask3 = mask1 | mask2
    res = m & mask3

    if val == 0:
        return res
    else:
        mask4 = 1 << n
        return mask4 | res

print(bin(set_value_of_nth_bit(0b11000011, 3, 1)))
print(bin(set_value_of_nth_bit(0b11000011, 1, 0)))
print(bin(set_value_of_nth_bit(0b11000011, 5, 1)))