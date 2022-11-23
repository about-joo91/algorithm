import sys
input = sys.stdin.readline

def char_to_int(char):
    return ord(char) - ord("a")

def insert(string):
    global unused
    cur = ROOT
    
    for char in string:
        cur_char_int = char_to_int(char)
        
        if nxt[cur][cur_char_int] == -1:
            nxt[cur][cur_char_int] = unused
            unused +=1
        cur = nxt[cur][cur_char_int]
    
    check[cur] = True

def is_in_origin_words(string):
    cur = ROOT
    
    for char in string:
        cur_char_int = char_to_int(char)
        if nxt[cur][cur_char_int] == -1:
            return False
        cur = nxt[cur][cur_char_int]
    return check[cur]

if __name__ == "__main__":
    N, M = map(int, input().split())
    ROOT = 1
    MX = 10000 * 500 + 5
    check = [False] * MX
    nxt = [[-1] * 26 for _ in range(MX)]
    unused = 2
    answer = 0
    
    for _ in range(N):
        insert(input())


    for _ in range(M):
        answer += int(is_in_origin_words(input()))
        
    print(answer)