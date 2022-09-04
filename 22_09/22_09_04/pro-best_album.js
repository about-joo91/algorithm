function solution(genres, plays) {
    
    let editedStructures = getEditedStructures(genres, plays);
    let play_sum = editedStructures[0]
    let genres_rank = editedStructures[1]

    let answer =  getAnswer(play_sum, genres_rank)
    return answer
    
}

const getEditedStructures = (genres, plays) => {
    let play_sum = {}
    let genres_rank = {}
    for (let i=0; i< genres.length; i++){
        play_sum[genres[i]] =  (play_sum[genres[i]] || 0) + plays[i]

        if(!genres_rank[genres[i]]) genres_rank[genres[i]] = []
        let album_info ={
            index : i,
            play : plays[i]
        }
        genres_rank[genres[i]].push(album_info)
    }
    return [play_sum, genres_rank]
}

const getAnswer  = (play_sum, genres_rank) => {
    var answer = [];
    let sorted_play_sum = []
    for (const key in play_sum){
        sorted_play_sum.push([key, play_sum[key]])
    }

    sorted_play_sum.sort((a,b) => b[1] - a[1])
    sorted_play_sum.forEach((data) => {
        genres_rank[data[0]].sort((a,b) => b.play - a.play)
        cur_rank = genres_rank[data[0]].splice(0, 2)
        for (let i=0; i< cur_rank.length; i++){
            answer.push(cur_rank[i].index)
        }
    })
    return answer;
}


console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))