N = int(input())

answers = []
for _ in range(N):
    answers.append(input())
answers = sorted(list(set(answers)),key = lambda x: (len(x) , x) )
for answer in answers:
    print(answer)