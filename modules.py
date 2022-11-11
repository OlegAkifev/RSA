def egcd(c, d):
    if c == 0:
        return d, 0, 1
    else:
        g, x, y = egcd(d % c, c)
        return g, y - (d // c) * x, x


# Ищем обратный элемент в кольце по модулю
def find_inverse_elem(k, p):
    g, x, _ = egcd(k, p)
    if g == 1:
        return x % p


# НОД
def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


# Возведение в степень по модулю
def power_mod(b, e, m):
    x = 1
    while e > 0:
        if e % 2:
            b, e, x = (b * b) % m, e // 2, (b * x) % m
        else:
            b, e, x = (b * b) % m, e // 2, x

    return x
