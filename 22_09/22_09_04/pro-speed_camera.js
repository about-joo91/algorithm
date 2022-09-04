function solution(routes) {

    routes.sort((a, b) => a[1] - b[1] )

    let camera = -30001;
    cnt = 0
    for (i = 0; i < routes.length; i++){
        if (routes[i][0] > camera){
            cnt+=1
            camera = routes[i][1]
        }
    }
    return cnt
}
console.log(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))