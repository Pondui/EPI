def set_interval_of_bits(n, i, j):
    mask = 2**(j-i+1) - 1
    mask = mask << i
    return n | mask

print(bin(set_interval_of_bits(0b11001100, 4, 5)))
print(bin(set_interval_of_bits(0b10000000, 1, 4)))
print(bin(set_interval_of_bits(0b10010011, 2, 3)))