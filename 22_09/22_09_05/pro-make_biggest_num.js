function solution(numbers, k) {
    const stack = [];
    let answer = '';

    for(let i=0; i< numbers.length; i++){
        let number = numbers[i]
        while(k>0 && stack[stack.length-1] < number){
            k--;
            stack.pop()
        }
        stack.push(number)
    }
    answer = stack.join("")
    return answer
}

console.log(solution("4177252841", 4))