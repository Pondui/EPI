def clear_n_bits_from_left(m, n):
    if m >= 0:
        bin_arr_len = len(bin(m)) - 2
    else:
        bin_arr_len = len(bin(m)) - 3

    mask = 2**bin_arr_len - 1
    mask2 = mask >> n
    return bin(mask2 & m)

print(clear_n_bits_from_left(-200, 4))
# This is a bit tricky because of the way that python handles negative numbers.
# Calculations work if you take negatives to be are the 2s complement of their positive counterparts.
# But python does not expose the leftmost bit, which when set to 0 represents positive, and when set to 1 represents negative.
# Even though python does not use sign-magnitude representation, the value of the leftmost bit still determines if a number is positive or negative.
# This is a natural consequence of 2s complement representation.

    
