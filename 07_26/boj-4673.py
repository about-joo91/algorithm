generated_num = []

for num in range(1, 10001):
    for i in str(num):
        num += int(i)
    generated_num.append(num)
for i in range(1, 10001):
    if i not in generated_num:
        print(i)