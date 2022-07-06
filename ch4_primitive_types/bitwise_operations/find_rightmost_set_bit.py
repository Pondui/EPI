def find_rightmost_set_bit(n):
    count = 0
    max_index = len(bin(n)) - 3
    while n & 1 == 0:
        n = n >> 1
        count += 1
    
    if count > max_index:
        return -1

    return count


print(find_rightmost_set_bit(10)) # 0b1010
print(find_rightmost_set_bit(248)) # 0b11111000
print(find_rightmost_set_bit(399)) # 0b110001111