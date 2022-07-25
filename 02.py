num1 = int(input())
num2 = input()

for i in range(-1, -len(num2)-1, -1):
    partial_of_num = int(num2[i])
    print(num1 * partial_of_num)
print(num1 * int(num2))