N= int(input())

numbers = sorted(list(set(map(int, input().split()))))

print(" ".join(map(str, numbers)))