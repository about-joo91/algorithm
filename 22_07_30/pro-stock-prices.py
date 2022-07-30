from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        for idx, next_price in enumerate(prices):
            if price > next_price:
                answer.append(idx+1)
                break
        else:
            answer.append(len(prices))
    return answer