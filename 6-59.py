sequence = []
number = int(input("Введите число: "))


while number != 100:
    sequence.append(number)
    number = int(input("Введите число: "))


if 77 in sequence:
    first_index = sequence.index(77) + 1
    print(f"Число 77 найдено в последовательности на позиции {first_index}.")
else:
    print("Число 77 не найдено в последовательности.")
