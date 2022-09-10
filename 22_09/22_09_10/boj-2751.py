###### 병합정렬로 구현 #######
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = j = 0
    
    merged_arr = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i+=1
        else:
            merged_arr.append(right[j])
            j+=1
        
    merged_arr += left[i:]
    merged_arr += right[j:]
    return merged_arr

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

for number in merge_sort(numbers):
    print(number)


####### 내장 정렬 ########
import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

for number in numbers:
    print(number)