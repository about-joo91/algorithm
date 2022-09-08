words = list(input())

i = 0
while i < len(words):
    if "<" == words[i]:
        i+=1
        while words[i] != ">":
            i+=1
        i+=1
    elif words[i].isalnum():
        start = i
        while i < len(words) and words[i].isalnum():
            i+=1
        words[start:i] = words[start:i][::-1]
    else:
        i+=1
print("".join(words))