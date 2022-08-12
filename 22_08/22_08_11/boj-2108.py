import sys
from collections import Counter
iter_num = int(sys.stdin.readline())
nums = []
for _ in range(iter_num):
    nums.append(int(sys.stdin.readline()))
nums.sort()
counter_nums = Counter(nums).most_common()
print(round(sum(nums) / iter_num))
print(nums[len(nums)//2])
if len(counter_nums) > 1:
    if counter_nums[0][1] == counter_nums[1][1]:
        print(counter_nums[1][0])
    else:
        print(counter_nums[0][0])
else:
    print(counter_nums[0][0])
print(nums[-1] - nums[0])