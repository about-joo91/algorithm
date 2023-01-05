KOR = 1
ENG = 2
MATH = 3
NAME = 0

N = int(input())
students = []
for _ in range(N):
    student_info = input().split()
    student_info = [student_info[0]] + list(map(int, student_info[1:]))
    students.append(student_info)



students = sorted(students, key=lambda x : (-x[KOR], x[ENG], -x[MATH], x[NAME]))


for student in students:
    print(student[NAME])