
# 초기 아이디어 따로 스택을 만들어 스택에 저장된 값을 불러와
# 웨이트 값과 곱한 후 다시 스택에 넣어주는 방식으로 구했으나
# 메모리 초과
import sys
input = sys.stdin.readline

zipped_datas = list(input())
unzip_stack = []
while zipped_datas:
    print(unzip_stack)
    cur_data = zipped_datas.pop()
    if cur_data == ")":
        continue
    elif cur_data == "(":
        weight = zipped_datas.pop()
        unzip_data = ""
        while unzip_stack:
            unzip_data += unzip_stack.pop()
        unzip_stack.append(unzip_data * int(weight))
    else:
        unzip_stack.append(cur_data) 
print(len("".join(unzip_stack)))


# 괄호 안 연산이 반복되는 것 같아서 재귀를 통해서 내부 값을 가져오면 좋겠다고 생각했고
# unzip 함수를 만들어서 동일한 연산에 대한 값을 가져오기위해 만들었으나 다시 메모리 초과
# 그래서 생각해보니 문자열을 굳이 만들어낼 이유가 없다.
# 길이값을 구하는 것이기 때문에 그냥 길이값만 구하기 위해서 로직을 좀 바꾸니 통과했다.
import sys
input = sys.stdin.readline

zipped_datas = list(input())
def unzip(length, zipped_datas):
    while zipped_datas:
        cur_data = zipped_datas.pop()
        if cur_data == ")":
            length += unzip(0, zipped_datas)
        elif cur_data == "(":
            weight = int(zipped_datas.pop())
            return length * weight
        else:
            length+=1
    return length
print(unzip(0, zipped_datas))