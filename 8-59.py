def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


fractions = []
for denominator in range(2, 8):
    for numerator in range(1, denominator):
        if gcd(numerator, denominator) == 1:
            fractions.append((numerator, denominator))

print("Простые несократимые дроби с знаменателем, не превышающим 7:")
for fraction in fractions:
    print(f"{fraction[0]}/{fraction[1]}")
