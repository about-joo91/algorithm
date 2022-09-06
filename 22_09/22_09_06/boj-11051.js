
const solution = (n, r) => {
    const dp = Array.from(Array(n+1), () => new Array(r+1).fill(0))

    let answer = binomial(n,r,dp)
    return answer
}
const binomial = (n, r, dp) => {
    if (dp[n][r] > 0) return dp[n][r]
    if (n === r || r === 0) return 1;
    else return dp[n][r] = binomial(n-1, r-1, dp) + binomial(n-1, r, dp);
}


console.log(solution(5, 2))
