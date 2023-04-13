A, B = map(int, input().split())

if A > B:
    A, B = B, A

def get_GCD(a, b):
    mod = a % b
    
    if mod == 0:
        return b
    
    return get_GCD(b, mod)

print("1" * get_GCD(A, B))