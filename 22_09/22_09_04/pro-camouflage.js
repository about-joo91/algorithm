function solution(clothes) {
    var answer = 1;
    let camouflage ={};
    for (let i = 0; i < clothes.length; i++){
        camouflage[clothes[i][1]] = (camouflage[clothes[i][1]] || 1) +1;
    }
    for (const key in camouflage){
        answer *= camouflage[key]
    }
    return answer -1;
}

console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
