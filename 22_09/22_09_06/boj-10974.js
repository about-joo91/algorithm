const solution = (N, depth=0) =>{
    const answer = []
    const back_tracking = (arr) =>{
        if(arr.length == N){
            answer.push(arr.join(" "))
            return
        }else{
            for (let i= 1; i<= N; i++){
                if(!arr.includes(i)){
                    arr.push(i);
                    back_tracking(arr)
                    arr.pop();
                }
            }
        }
    }
    back_tracking([])
    console.log(answer)
}


solution(3)