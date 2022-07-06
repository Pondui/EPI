def clear_rightmost_set_bit(n):
    return bin(n & (n-1))

clear_rightmost_set_bit(100)
clear_rightmost_set_bit(250)