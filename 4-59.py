
number = int(input("Введите четырехзначное число: "))

if '4' in str(number):
    print("Цифра 4 входит в число")
else:
    print("Цифра 4 не входит в число")

b = int(input("Введите цифру для проверки: "))

if str(b) in str(number):
    print(f"Цифра {b} входит в число")
else:
    print(f"Цифра {b} не входит в число")
