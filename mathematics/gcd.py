# First Approach
# Euclidean Algorithm

def gcd1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = 15
b = 12

print(gcd1(a, b))


def gcd2(a, b):
    if b == 0:
        return a

    return gcd2(b, a % b)


print(gcd2(a, b))
