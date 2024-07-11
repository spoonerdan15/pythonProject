def custom_floor(x):
    if x >= 0:
        return int(x)
    else:
        return int(x) - 1


def custom_sin(x):
    # sin(x) ≈ x - x^3/3! + x^5/5! - x^7/7!
    x = x % (2 * 3.141592653589793)  # Modulo 2π
    term = x
    sine = x
    for i in range(1, 10):
        term *= -x * x / (2 * i * (2 * i + 1))
        sine += term
    return sine


def calculate_f(x):
    sin_x = custom_sin(x)

    if sin_x >= 0:
        k = x ** 2
    else:
        k = custom_floor(x)

    if x < k:
        f = custom_floor(x)
    else:
        f = k * x

    return f


x_values = [-3.5, -2.1, 0, 1.5, 3]
for x in x_values:
    print(f"f({x}) = {calculate_f(x)}")