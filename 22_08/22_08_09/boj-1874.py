import sys
iter_num = int(input())
stack = []
answers = []
limit_nums = [x for x in range(iter_num, 0, -1)]
for i in range(iter_num):
    num_now = int(input())
    while limit_nums and stack[-1:] != [num_now]:
        stack.append(limit_nums.pop())
        answers.append('+')
    if stack[-1] != num_now:
        print("NO")
        sys.exit(0)
    stack.pop()
    answers.append("-")
for answer in answers:
    print(answer)