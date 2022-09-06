const solution = (haebinClothes) => {
    let answer = 1
    const clothesMap = {}
    for(let i=0; i < haebinClothes.length; i++){
        let clothes = haebinClothes[i];
        clothesMap[clothes[1]] = (clothesMap[clothes[1]] || 1) +1
    }
    for (const key in clothesMap){
        answer *= clothesMap[key]
    }
    return answer -1
}

console.log(solution(
    [['hat', 'headgear'],
    ['sunglasses', 'eyewear'],
    ['turban', 'headgear'],]))