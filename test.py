import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/test.txt','r')
N = int(input())

for _ in range(N):
    left = []
    right = []
    kang_input = list(input())

    for char in kang_input:
        if char == "<":
            if left: right.append(left.pop())
        elif char == ">":
            if right: left.append(right.pop())
        elif char == "-":
            if left: left.pop()
        else:
            left.append(char)

    print("".join(left)+ "".join(reversed(right)))