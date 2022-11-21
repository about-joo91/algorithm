## 알고리즘 설명
### 패턴 매칭 문제 

아래와 같이 A안에 B가 있는지 확인하는 알고리즘이다.
A = [o, r, o, n, d, o, n, t, i, s, s]
B = [n, t, i]

kmp를 모르는 이 상태에서 B가 A안에 있음을 어떻게 확인할 수 있을까? A를 순회하면서 B와 매칭되는지 검사하면 찾을 수 있다.

이런 방식은 단순하면서도 일반적인 상황에서 잘 작동한다. 그러나 이 구현의 최악의 시간복잡도를 한 번 생각해보자.(앞으로도 본인 코드에대해 최악의 상황에 대한 시간복잡도를 찾아 내면 시간복잡도 분석에도 반례를 잡아낼 때도 좋다.)

A  = [a, a, a, a, a, a, a, a, a, a, a]
B = [a, a, a, a, a, b]

이 상황이 최악의 예시라고 볼 수 있다. 끝까지 가서야 틀렸다는 사실을 알 수 있고 이 검사는 A전체를 돌 동안 계속되기 때문에 최악의 경우 O(A의 길이 x B의 길이) 에 동작한다.


* KMP란 이러한 패턴 매칭 문제를 O(A의길이 + B의 길이)에 해결할 수 있는 기적의 알고리즘
* 굉장히 헷갈림
* 먼저 KMP에서 쓰이는 *실패함수*를 알면 KMP를 이해하는데 도움이 됨

### 실패함수
실패함수 F(x) -> 문자열 S[0:x+1]에서 접두사와 접미사가 일치하는 최대 길이

S = [a, b, a, b, c, a, b, a, b ,a]
F(2)에 대한 예시
 a *b a* 접미사
*a b* a 접두사
F(2) != 2
F(1)
a b *a* 접미사
*a* b a  접두사
F(2) = 1


이 실패함수를 어떻게 구해야할까?
1. 가장 쉬운 방법
F(5)를 구한다고 하면 F(5) = 5인지 아니라면 F(5) = 4인지 하나하나 확인하는 방법이 있다. 이렇게 계산을 하면 각 F(x)에 대해서 O(S의 길이 ** 2) 만큼의 연산이 필요하기 때문에 총 O(S의 길이 ** 3)에 값을 구할 수 있다.
2. 이전 결과값을 활용하기
 a b a b c *a*
*a* b a b  c a
이 결과를 통해서 F(5) = 1임을 알 수 있다. 

F(6)을 구하기 위해서 F(5)를 어떻게 활용할 수 있을까?
a b a b c *a b*
*a b* a b c a b
끝에 	b가 추가 되었고 생각해보면 F(5)에 이미 일치함을 찾아냈던 a가 다시 쓰인다는 것을 알 수 있다. 이 a가 추가되어 a b가 일치하게 되었고 F(6) = 2임을 알 수 있다.

이 예시를 통해서 일반화 하면 F(k) = 최대 F(k-1)+1이 된다.

추가된 값이 일치한다는 아주 좋은 예시도 있지만 일치하지 않을 수 있다. 
a b a b c *a b a b a*
*a b a b c* a b a b a

이렇게 이전 F(8)은 4임을 알고 마지막 값이 일치 하지 않을 때 구하는 방법은

*a b a b c* a b a b a
  *a b a b c* a b a b a

원래 값을 제쳐두고 비교할 값을 한칸 뒤로 밀어서 생각해보자.
a*bab*
*aba*b

ab*ab*
*ab*ab

볼드처리가 된 부분만 보면서 한칸씩 밀어서 옮기다보면 결국 앞서 구했던 F(3)에서 일치했던 값을 추출해 낼 수 있다. 즉 접미사와 접두사가 일치하는 값이 최소 2임을 알 수 있고 3번째 인덱스 값의 비교를 통해서 F(9)의 값이 3인지 아니면 한 번 더 아래로 내려가서 값을 구해야하는지 알 수 있다.

```python
def failure(s):
    f = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]: j = f[j-1]
        if s[i] == s[j]:
            j+=1
            f[i] = j
    return f
```

실패함수의 이해가 고통이었던 것과 다르게 소스코드는 말도 안되게 간단하다. 

### KMP
최종적으로 실패함수를 활용해서 KMP를 구해보자.

S = ABABABADABABACABAD
P = ABABACABA


S안에 P가 있는지 알아보기 위해서 하나씩 검사를 해보자

S를 확인하는 인덱스를 i로 놓고 P를 확인하는 인덱스를 j로 놓으면 하나씩 증가시켜가면서 검사를 해보면 처음 ABABA까지는 일치함을 알 수 있다. 

이때 i와 j의 인덱스는 모두 5이다. 여기서 실패함수테이블을 어떻게 활용할 수 있을까?

실패함수 테이블을 한 번 보면 0 0 1 2 3 0 1 2 3이라는 결과를 가지고 있다.

현재 길이 5까지의 접미사와 접두사 중복되는 지점 즉 스타트지점은 어디일까? 
실패함수 4는 아래와 같은 결과로 3을 갖는다.
AB*ABA*
*ABA*BA
즉, 우리는 실패함수 테이블을 통해서 현재 i의 인덱스 -3 위치에 ABA가 중복되고 있음을 유추할 수 있다. 따라서 실패함수를 구할 때와 마찬가지로 failure_table[j-1] 를 다시 j로 놓고 i 인덱스에 있는 S의 알파벳과 j인덱스에 있는 P의 알파벳이 일치하는지 다시 확인한다. 만약 끝까지 일치하는 문자열이 있다면 그건 P가 S의 부분문자열임을 알 수 있다.

### 연습문제
boj-16916
```python
def get_failure_table(s):
    f = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]: j = f[j-1]
        if s[i] == s[j]:
            j+=1
            f[i] = j
    return f

def is_substring(string:str, might_sub_string:str, failure_table:list[int]) -> bool:
    j = 0
    
    for i in range(len(string)):
        while j > 0 and string[i] != might_sub_string[j]: j = failure_table[j-1]
        if string[i] == might_sub_string[j]: j+=1
        if j == len(might_sub_string): return True
    return False
if __name__ == '__main__':
    S = input()
    P = input()
    failure_table = get_failure_table(P)
    print(int(is_substring(S, P, failure_table)))
```