function solution(distance, rocks, n) {
    rocks.sort((a,b) => a - b)
    rocks.push(distance)

    let left = 0;
    let right = distance;
    let answer = 0;

    while (left <= right){
        
        mid = Math.floor((left + right) /2)
        let min_distance = Infinity
        cur = 0
        remove_cnt = 0

        for (let i =0; i < rocks.length; i++){
            diff = rocks[i] - cur
            if (diff < mid) remove_cnt +=1
            else{
                cur = rocks[i]
                min_distance = Math.min(min_distance, diff)
            }
        }
        if (remove_cnt > n) {
            right = mid -1
        }else{
            answer = min_distance
            left= mid+1
        }
    }
    return answer;
}

console.log(solution(25, [2, 14, 11, 21, 17], 2))