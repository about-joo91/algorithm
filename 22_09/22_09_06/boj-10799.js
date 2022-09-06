const solution = (strings) => {
    answer = 0
    const stack =[];
    for (let i =0; i< strings.length; i++){
        if (strings[i] == '(') {
            stack.push('(')
        }else {
            if (strings[i-1] == '('){
                stack.pop()
                answer += stack.length;
            }else {
                stack.pop()
                answer +=1
            }
        }
    }
    return answer
}

console.log(solution("(((()(()()))(())()))(()())"))