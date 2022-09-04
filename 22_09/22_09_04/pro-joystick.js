const changeMinAscii = (ascii) => {
    let fromA = 'A'.charCodeAt(0)
    let fromZ = 'Z'.charCodeAt(0) +1
    return Math.min(ascii - fromA, fromZ - ascii)
}

function solution(name) {
    let answer = 0;
    let N = name.length;
    let minMoves = N-1;

    for (let i=0; i < N; i++){

        answer += changeMinAscii(name.charCodeAt(i));

        let next_idx = i+1;
        while (next_idx < N && name[next_idx] == 'A') next_idx++;
        minMoves = Math.min(minMoves, (i*2) + N - next_idx)
        minMoves = Math.min(minMoves, (N-next_idx) * 2 +i) 
    }

    return answer + minMoves
}


console.log(solution("JEROEN"))
