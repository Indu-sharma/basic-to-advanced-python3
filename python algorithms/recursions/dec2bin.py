def dec2bin(n):
    if n == 0:
        return n

    return n % 2 + 10 * dec2bin(n // 2)


print(dec2bin(7))
