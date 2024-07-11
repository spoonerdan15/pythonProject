import random

# Генерация случайных возрастов для учеников первого класса
ages_class1 = [random.uniform(13, 16) for _ in range(20)]

# Генерация случайных возрастов для учеников второго класса
ages_class2 = [random.uniform(13, 16) for _ in range(20)]

# Вычисление среднего возраста для каждого класса
average_age_class1 = sum(ages_class1) / len(ages_class1)
average_age_class2 = sum(ages_class2) / len(ages_class2)

print(f"Средний возраст учеников первого класса: {average_age_class1:.2f} лет")
print(f"Средний возраст учеников второго класса: {average_age_class2:.2f} лет")
