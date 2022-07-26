iter_num = int(input())
for _ in range(iter_num):
    grades = list(map(int, input().split()))
    len_grades = grades.pop(0)
    avg = sum(grades) // len_grades
    over_avgs = list(filter(lambda x : x > avg , grades))
    print("{:.3f}%".format(len(over_avgs)/ len(grades) * 100))