def full(a, b, c):
    d = b**2 - (4 * a * c)
    x = (-b + (d ** 0.5)) / (2 * a)
    y = (-b - (d ** 0.5)) / (2 * a)
    return [x, y]


def ab(a, b):
    x = -b / a
    return [0, x]


def ac(a, c):
    x = (-c / a) ** 0.5
    return [x]


def bc(b, c):
    x = -c / b
    return [x]
