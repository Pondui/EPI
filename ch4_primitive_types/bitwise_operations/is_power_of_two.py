from operator import truediv


def is_power_of_two(n):
    if n & (n-1) == 0:
        return True
    else:
        return False

print(is_power_of_two(0))
print(is_power_of_two(4))
print(is_power_of_two(8))
print(is_power_of_two(10))
print(is_power_of_two(200))