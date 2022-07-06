def find_rightmost_empty_bit(n):
    count = 0
    max_index = len(bin(n)) - 3
    while 1 & n != 0:
        n = n >> 1
        count += 1
        
    if count > max_index:
        return -1

    return count

print(find_rightmost_empty_bit(10)) # 0b1010
print(find_rightmost_empty_bit(250)) # 0b11111010
print(find_rightmost_empty_bit(399)) # 0b110001111