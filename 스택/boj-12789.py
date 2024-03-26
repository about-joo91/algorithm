n = int(input())
students = list(map(int, input().split(' ')))

stack = []
current = 1
for student in students:
    stack.append(student)

    while stack and stack[-1] == current:
        stack.pop()
        current+=1

print('Nice' if not stack else 'Sad')
