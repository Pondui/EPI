def get_value_of_nth_bit(m, n):
    if n > len(bin(m)) - 3:
        return -1

    mask = 1 << n
    if m & mask > 0:
        return 1
    else:
        return 0

print(bin(678), get_value_of_nth_bit(678, 0))
print(bin(678), get_value_of_nth_bit(678, 5))
print(bin(678), get_value_of_nth_bit(678, 10))