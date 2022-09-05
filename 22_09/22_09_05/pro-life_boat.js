function solution(people, limit) {
    people.sort((a,b) => a-b)
    let small = 0
    let big = people.length-1;
    cnt = 0
    while (small <= big){
        if (people[small] + people[big] <=limit){
            small++;
        }
        big--;
        cnt++;
    }
    return cnt
}

console.log(solution([70, 50, 80, 50], 100))