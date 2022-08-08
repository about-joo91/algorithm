def recursive(names,i,n, answer):
    if i == len(names):
        answer.append(n)
        return
    recursive(names, i+1, n+ ord(names[i])- ord('A')+1, answer)
    back = len(names) - i-1
    recursive(names, i+1, n + ord(names[back])- ord('A') + i , answer )
def solution(name):
    names = list(name)
    answer =[]
    n = ord(names[0])- ord('A')
    recursive(names,1,n,answer)
    return min(answer)

print(solution("JEROEN"))