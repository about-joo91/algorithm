import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
wanted_cards = list(map(int, input().split()))
hash_map = {}

for card in cards:
    if card in hash_map:
        hash_map[card] +=1
    else:
        hash_map[card] =1

print(' '.join(str(hash_map[wanted_card]) if wanted_card in hash_map else "0" for wanted_card in wanted_cards))