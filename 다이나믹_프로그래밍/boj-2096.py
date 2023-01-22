import sys
input = sys.stdin.readline

N = int(input())
maps = list(map(int, input().split()))
m_dp = maps[:] 
M_dp = maps[:]

for i in range(N-1):
    fir, sec, third = map(int, input().split())
    
    m_dp = [fir + min(m_dp[0], m_dp[1]), sec + min(m_dp), third + min(m_dp[1], m_dp[2])]
    M_dp = [fir + max(M_dp[0], M_dp[1]), sec + max(M_dp), third + max(M_dp[1], M_dp[2])]

print(f"{max(M_dp)} {min(m_dp)}")