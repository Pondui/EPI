def clear_first_n_bits(bitarr, n):
    ''' Clear bits 0 to n inclusive '''
    mask = 2**(n+1) - 1
    mask = ~mask
    res = bitarr & mask
    return res

if clear_first_n_bits(0b11010110, 3) == 0b11010000:
    print("pass")
else:
    print("false", str(int(0b11010110)))

if clear_first_n_bits(0b11101111, 4) == 0b11100000:
    print("pass")
else:
    print("false", str(int(0b11101111)))

if clear_first_n_bits(0b01010010, 1) == 0b01010000:
    print("pass")
else:
    print("false", str(int(0b01010000)))