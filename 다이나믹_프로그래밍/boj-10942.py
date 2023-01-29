def get_is_palindrome_of_whole_num_of_cases():
    for i in range(N):
        for j in range(2):
            left = i
            right = i + j
            while left >= 0 and right < N:
                if numbers[left] == numbers[right]: is_pal[left][right] = 1
                else: break
                left -= 1
                right += 1
    

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())

    is_pal = [[0] * N for _ in range(N)]
    get_is_palindrome_of_whole_num_of_cases()
    
    for _ in range(M):
        start, end = map(int, input().split())
        print(is_pal[start-1][end-1])

