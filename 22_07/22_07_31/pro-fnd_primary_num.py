from itertools import permutations
def solution(numbers):
    numbers = list(numbers)
    answers = []
    for i in range(1, len(numbers)+1):
        answers += [int(''.join(x)) for x in list(permutations(numbers,i))]
    answers = list(set(answers))
    prime_cnt = 0
    for answer in answers:
        if answer ==1 or answer == 0 : continue
        for i in range(2, (int(answer**(1/2)))+1):
            if answer % i ==0:
                break
        else:
            prime_cnt+=1
    return prime_cnt
print(solution("011"))