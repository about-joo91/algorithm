import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
wanted_cards = list(map(int, input().split()))
answers = []
for wanted_card in wanted_cards:
    left, right = 0, len(cards)-1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == wanted_card:
            answers.append("1")
            break
        if cards[mid] >= wanted_card:
            right = mid -1
        else: left = mid+1
    else: answers.append("0")
print(" ".join(answers))