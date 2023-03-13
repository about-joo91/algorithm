import sys
input = sys.stdin.readline

def append_possible_numbers(depth, arr):
    if depth == 3:
        possible_numbers.append(arr)
        return
    
    for i in range(1, 10):
        if i not in used:
            used.append(i)
            append_possible_numbers(depth+1, arr + [i])
            used.pop()
    

N = int(input())
possible_numbers = []

used = []
append_possible_numbers(0,[])
possible_check = [True] * len(possible_numbers)
for _ in range(N):
    number, strike, ball = input().split()
    for i in range(len(possible_numbers)):
        s_check = b_check = 0
        for j in range(3):
            if possible_numbers[i][j] == int(number[j]):
                s_check +=1
            elif int(number[j]) in possible_numbers[i]:
                b_check +=1
        if (s_check != int(strike)) or (b_check != int(ball)):
            possible_check[i] = False

print(sum(possible_check))
