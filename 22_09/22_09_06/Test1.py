def solution(heights):
    cnt = 0
    for idx, height in enumerate(heights):
        stack_right = []
        maximum_right = height
        for comparison in heights[idx+1:]:
            if comparison >= maximum_right and comparison not in stack_right:
                cnt+=1
                stack_right.append(comparison)
                maximum_right = comparison
        
        stack_left = []
        maximum_left = height
        for comparison in reversed(heights[:idx]):
            if comparison >= maximum_left  and comparison not in stack_left:
                cnt+=1
                stack_left.append(comparison)
                maximum_left = comparison
    print(cnt)


solution([5,5,5])