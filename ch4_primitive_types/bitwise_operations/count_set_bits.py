# Time complexity of O(n) where n is the bit array length
def count_set_bits_On(m):
    count = 0
    while m > 0:
        if (m & 1) == 1:
            count += 1
        m = m >> 1
    return count

# Time complexity of O(set) where set is the number of set bits
def count_set_bit_0set(m):
    count = 0
    while m > 0:
        m = m & (m - 1)
        count += 1
    return count

# 0b1010, 2 set bits
print(count_set_bits_On(10))
print(count_set_bit_0set(10))

# 0b1100100, 3 set bits
print(count_set_bits_On(100))
print(count_set_bit_0set(100))

# 0b1111101000, 6 set bits
print(count_set_bits_On(1000))
print(count_set_bit_0set(1000))