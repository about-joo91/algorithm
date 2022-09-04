function solution(n) {
    let dp = Array(n+1).fill(0)
    dp[0] = 1
    dp[1] = 1
    for (let i =2; i< n+1; i++){
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    }
    return dp[n] 
}

console.log(solution(9))
