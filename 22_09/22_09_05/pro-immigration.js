function solution(n, times) {
    let answer = 0;
    let left = Math.min(...times)
    let right = Math.max(...times) * n

    while (left <= right){
        let mid = Math.floor((left + right)/2)
        let check_cnt = 0

        for (let i=0; i<times.length; i++){
            let time = times[i]
            check_cnt += Math.floor(mid/time);
            if (check_cnt >= n) break;
        }
        if (check_cnt >= n){
            answer = mid
            right = mid - 1
        }else {
            left = mid+1
        }
    }
    return answer;
}

console.log(solution(6, [7,10]))