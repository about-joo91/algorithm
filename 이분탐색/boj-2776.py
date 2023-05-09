T = int(input())
for _ in range(T):
    N = int(input())
    note_one = sorted(list(map(int, input().split())))
    M = int(input())
    note_two = list(map(int, input().split()))


    def is_target_in_note_one(target):
        left = 0
        right = N-1

        while left <= right:
            mid = (left + right) //2
            if note_one[mid] == target:
                return True
            elif note_one[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    for number in note_two:
        print(int(is_target_in_note_one(number)))
