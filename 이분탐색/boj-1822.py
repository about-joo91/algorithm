def is_target_in_array(arr, target):
    start, end = 0, len(arr)-1
    
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target: return True
        elif arr[mid] > target: end = mid-1
        else: start = mid+1
    return False


if __name__ == '__main__':
    N, M = map(int,input().split())

    first = list(map(int,input().split()))
    second = sorted(list(map(int, input().split())))
    
    answers = []
    for first_value in first:
        if not is_target_in_array(second, first_value):
            answers.append(first_value)

    if answers:
        print(len(answers))
        print(*sorted(answers))
    else: print(0)