def factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result

def calculate_sum(n):
    sum_result = 1.0
    for i in range(1, n + 1):
        sum_result += 1 / factorial(i)
    return sum_result


n = int(input("Введите значение n, где 1 < n <= 10: "))


if 1 < n <= 10:
    result = calculate_sum(n)
    print(f"The sum is: {result}")
else:
    print("The value of n should be between 1 and 10 (exclusive).")