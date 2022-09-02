string = input()
k = int(input())
iter_num = len(string) // k
for i in range(iter_num):
    characters = list(string[i*k:(i+1)* k])
    check = []
    for character in characters:
        if character not in check:
            check.append(character)
    print("".join(check))