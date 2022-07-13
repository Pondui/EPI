# n-1 has all bits after (and including) the rightmost set bit flipped
# Taking the ~ of this means that all bits before the rightmost set bit are now flipped relative to n, and all bits after (and including)
# the rightmost set bit are the original bits in n (i.e the last set bit and trailing 0s)

def value_of_rightmost_set_bit(n):
    ''' Returns the index of the leftmost set bit'''
    return n & ~(n-1)

print(value_of_rightmost_set_bit(0b10000))
print(value_of_rightmost_set_bit(0b10010))
print(value_of_rightmost_set_bit(0b11001000))
