import sys

if __name__ == '__main__':
    sys.stdin = open('', 'r')
    N, M = map(int, input().split())

    name_number_map = {}
    pocket_monters = []

    for i in range(1, N+1):
        name = input()
        pocket_monters.append(name)
        name_number_map[name] = i

    for _ in range(M):
        question = input()

        if question.isdigit():
            print(pocket_monters[int(question) - 1])
        else:
            print(name_number_map[question])