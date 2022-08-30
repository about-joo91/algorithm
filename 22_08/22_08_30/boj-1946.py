import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    len_of_applicants = int(input())
    grades = []
    for _ in range(len_of_applicants):
        grades.append(list(map(int,input().split())))
    
    grades.sort()
    comparison = grades[0][1]
    cnt = 1
    for j in range(1, len_of_applicants):
        if comparison > grades[j][1]:
            cnt+=1
            comparison = grades[j][1]       
    print(cnt)