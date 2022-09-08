N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []
def back():
    if len(answer) == M:
        print(" ".join(map(str, answer))) 
        return
    for number in numbers: 
        if number not in answer:
            answer.append(number) 
            back() 
            answer.pop()
back()