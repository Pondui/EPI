def set_first_n_bits(m, n):
    ''' Assumes n doesn't exceed the length of the bit array, counting from 0 e.g. n=3 means the 0th, 1st, 2nd, and 3rd bits are set '''
    mask = 2**(n+1) - 1
    return m | mask

print(bin(set_first_n_bits(0b1001011101010, 3)))
print(bin(set_first_n_bits(0b1010111000101, 5)))
print(bin(set_first_n_bits(0b1111001000010, 7)))