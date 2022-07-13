# We know that if we take x and take away 1, i.e. x - 1, all bits (after and including) the last set bit are flipped
# We can take advantage of this fact to clear the last set bit since the & of a bit and it's flipped counterpart is always
# If we take x and add 1, i.e. x + 1. all bits up to and including the first 0 are flipped
# We use this, together with the | operator to set the lowermost 0
def set_rightmost_empty_bit(n):
    if len(bin((n+1))) > len(bin(n)):
        return n
    else:
        return n | n + 1

print(bin(set_rightmost_empty_bit(0b110011)))
print(bin(set_rightmost_empty_bit(0b111111)))
print(bin(set_rightmost_empty_bit(0b101111)))