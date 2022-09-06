const solution = (N, M, numbers, ranges) => {
    let tmpSum = 0;
    const prefixSums= [0]
    for (let i =0; i < N; i++){
        tmpSum += numbers[i]
        prefixSums.push(tmpSum)
    }
    for (let i = 0; i< M; i++){
        const [left , right] = ranges[i]
        console.log(prefixSums[right] - prefixSums[left-1])
    }

}

solution(5, 3, [5,4,3,2,1], [[1,3], [2,4], [5,5]])