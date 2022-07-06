def clear_interval_of_bits(n, i, j):
    ''' Clear an interval from i to j-1 inclusive '''
    # Note that we can also get mask1 by doing (1 << i) - 1
    mask1 = 2**i - 1
    mask2 = ~0 << (j + 1)
    mask3 = mask1 | mask2
    ans = n & mask3 
    return ans

print(bin(clear_interval_of_bits(100, 2, 5)))
# 100 in binary is 1100100
# Clearing bits 2 to 5 inclusive should yield 1000000

print(bin(clear_interval_of_bits(125, 3, 4)))
# 125 in binary is 1111101
# Clearing bits 3 to 4 inclusive should yield 1100101

print(bin(clear_interval_of_bits(255, 4, 7)))
# 255 in binary is 11111111
# Clearing bits 4 to 7 inclusive should yield 00001111