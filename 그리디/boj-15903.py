import heapq

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
heapq.heapify(numbers)

while M:
    first_minimum = heapq.heappop(numbers)
    seconde_minimum = heapq.heappop(numbers)
    
    for i in range(2):
        heapq.heappush(numbers, first_minimum + seconde_minimum)
        
    M-=1
        
print(sum(numbers))