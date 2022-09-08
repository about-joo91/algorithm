N = int(input())
answer = []
def back():
    if len(answer) == N:
        print(" ".join(map(str, answer))) 
        return
    for number in range(1, N+1): 
        if number not in answer:
            answer.append(number) 
            back() 
            answer.pop()
back()