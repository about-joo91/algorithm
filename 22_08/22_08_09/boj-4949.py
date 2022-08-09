check_sign_front = ['(', '[']
check_sign_back = [')',']']
while True:
    sentence = input()
    if sentence[0] == ".":
        break
    brackets_f = []
    for alpha in sentence:
        if alpha in check_sign_front:
            brackets_f.append(alpha)
        elif alpha in check_sign_back:
            if len(brackets_f) == 0 or (ord(alpha) - ord(brackets_f[-1])) > 2:
                print("no")
                break
            else:
                brackets_f.pop()
    else:
        if len(brackets_f) > 0:
            print("no")
        else:
            print("yes")