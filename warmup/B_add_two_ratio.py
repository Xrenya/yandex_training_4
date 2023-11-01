a, b, c, d = map(int, input().strip().split())


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def add(a, b, c, d):
    x = a * d + b * c
    y = b * d
    z = gcd(x, y)  # find the lowest common divisor
    return x // z, y // z

print(*add(a, b, c, d))
