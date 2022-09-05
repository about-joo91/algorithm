def solution(n, times):
    left = 0
    right = max(times) *n
    answer = 0
    
    while left <= right:
        mid = (left+ right) //2
        checked = 0
        for time in times:
            checked += mid // time

            if checked >= n:
                break
        if checked >= n:
            answer = mid
            right = mid-1
        elif checked < n:
            left = mid+1
        
            
    return answer