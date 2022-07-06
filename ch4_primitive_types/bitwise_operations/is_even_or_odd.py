def is_even_or_odd(n):
    if n & 1 > 0:
        return "odd"
    else:
        return "even"

print(is_even_or_odd(5))
print(is_even_or_odd(10))
print(is_even_or_odd(15))