import sys
input = sys.stdin.readline
T = int(input())

def get_gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b:
        a, b = b, a % b
    
    return a


def get_pair_gcd(depth, pair, start):
    global answer
    if depth == 2:
        answer += get_gcd(*pair)
        return

    for i in range(start, len(numbers)):
        if not visisted[i]:
            visisted[i] = True
            get_pair_gcd(depth+1, pair+ [numbers[i]], i)
            visisted[i] = False
            
        

for _ in range(T):
    inputs = list(map(int, input().split()))
    N = inputs[0]
    numbers = inputs[1:]
    answer = 0
    visisted = [False] * N
    get_pair_gcd(0, [],0)
    print(answer)