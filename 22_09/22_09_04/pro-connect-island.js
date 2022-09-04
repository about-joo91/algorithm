function solution(n, costs) {
    var answer = 0;
    costs.sort((a, b) => a[2]-b[2]);
    const visited = new Array(n).fill(false);
    const bridge = new Array(costs.length).fill(false);
    

    visited[costs[0][0]] = true;
    visited[costs[0][1]] = true;
    answer += costs[0][2];

    let cnt = 1;

    while (cnt < n-1){
        for (let i=0; i < costs.length; i++){
            const [start ,end, cost] = costs[i];
            if (bridge[i]) continue;
            if (!visited[start] && visited[end] || visited[start] && !visited[end]){
                
                cnt+=1;
                bridge[i] = true;
                visited[start] = true;
                visited[end] = true;
                answer += cost;
                break;
            }
        }
    }
    
    return answer;
}


function solution(n, costs){
    let answer = 0;
    const parent = [];
    for (let i =0; i<n; i++) parent.push(i)
    
    costs.sort((a, b) => a[2] - b[2])

    const getParent = (parent, x) => {
        if(parent[x] === x) return x;
        return parent[x] = getParent(parent, parent[x])
    }

    const unionParent = (parent, x, y) => {
        const n1 = getParent(parent,x)
        const n2 = getParent(parent,y)
        if (n1 < n2) return parent[n2] = n1;
        else return parent[n1] = n2
    }

    const findParent = (parent, x, y) => {
        const n1 = getParent(parent,x)
        const n2 = getParent(parent,y)
        if (n1 == n2) return true;
        else return false;
    }

    for (const cost of costs){
        if(!findParent(parent, cost[0] , cost[1])){
            answer += cost[2];
            unionParent(parent,cost[0], cost[1])
        }
    }
    return answer;
}

console.log(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))