function solution(brown, yellow) {
    let total = brown + yellow
    var answer = [];
    
    for (let height = 3; height <= brown; height++){
        if (total % height === 0){

            let width = total / height;

            if ((height-2) * (width-2) === yellow){
                return [width, height]
            }
        }
    }
    return answer
}

console.log(solution(10, 2))