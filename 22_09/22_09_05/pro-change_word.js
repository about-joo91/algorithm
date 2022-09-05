function solution(begin, target, words) {
    let answer =  bfs(begin, target, words);
    return answer;
}

const bfs = (begin, target, words) => {
    const queue = [];
    const visited = [];

    queue.push([begin, 0])
    
    while (queue.length){
        let [word, cnt] = queue.shift();
        if (word === target) return cnt;

        words.forEach(nWord => {
            if (!visited.includes(nWord) && isDiffOne(word, nWord)){
                queue.push([nWord, ++cnt])
                visited.push(nWord)
            }
        })
    }
    return 0;
}

const isDiffOne = (word1, word2) => {
    let check = 0
    for (let i = 0; i < word1.length; i++) {
        if (word1[i] !== word2[i]) {
            check++;
        }
    }
    return check === 1
}

console.log(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))