string_map = {}

string = input()
N = len(string)

for i in range(1, N):
    for j in range(0, N-i+1):
        string_map[string[j:j+i]] = 1
        
print(len(string_map.keys()) +1)