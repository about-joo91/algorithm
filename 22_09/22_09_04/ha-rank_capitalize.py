def solve(s):
    names = s.split(' ')
    for i in range(len(names)):
        if len(names[i]) > 0:
            names[i] = names[i][0].upper() + names[i][1:]
    return " ".join(names)