
grades = []


for student in range(1, 19):
    print(f"Введите оценки ученика {student}:")
    student_grades = []
    for subject in range(1, 4):
        grade = int(input(f"  Предмет {subject}: "))
        student_grades.append(grade)
    grades.append(student_grades)


for student in range(1, 19):
    print(f"Оценки для ученика {student}: ", end="")
    for subject in range(1, 4):
        print(grades[student-1][subject-1], end=" ")
    print()