def flip_nth_bit(m, n):
    mask = 1 << n
    return XOR(mask, m)

def XOR(x, y):
    return (x & ~y | ~x & y)

print(flip_nth_bit(10, 3)) # 0b1010
print(flip_nth_bit(248, 5)) # 0b11111000
print(flip_nth_bit(399, 5)) # 0b110001111