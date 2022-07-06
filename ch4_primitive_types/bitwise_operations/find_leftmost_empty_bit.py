def find_leftmost_empty_bit(n):
    exponent = len(bin(n)) - 3
    mask = 2**exponent

    count = 0
    while mask & n != 0:
        n = n << 1
        count += 1
    
    index = exponent - count
    return index

print(find_leftmost_empty_bit(0b1110100))
print(find_leftmost_empty_bit(0b1011))
print(find_leftmost_empty_bit(0b1111000))