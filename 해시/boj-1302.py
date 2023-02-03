import sys
input = sys.stdin.readline
N = int(input())
book_map = {}
for _ in range(N):
    cur_book = input()
    if cur_book in book_map:
        book_map[cur_book]+=1
    else: book_map[cur_book] = 1


values = sorted(book_map.items(), key= lambda x: (-x[1], x[0]))
print(values[0][0])