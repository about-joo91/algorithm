T = int(input())

for _ in range(T):
    clothes_num = int(input())
    answer = 1
    fashion_map = {}
    
    for _ in range(clothes_num):
        clothes, category = input().split()
        if category in fashion_map:
            fashion_map[category] +=1
        else: fashion_map[category] = 1
    
    for key in fashion_map.keys():
        answer *= fashion_map[key]+1
    print(answer-1)