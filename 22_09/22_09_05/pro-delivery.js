const dijkstra = (distances, graph) => {
    let priority_queue =[];
    priority_queue.push({node : 1, dist : 0});
    distances[1] = 0;

    while (priority_queue.length !==0 ){
        priority_queue.sort((a, b) => a.dist - b.dist)
        const {node, dist} = priority_queue.shift();
        graph[node].forEach((next_node) => {
            if(distances[next_node.node] > distances[node] + next_node.dist){
                distances[next_node.node] = distances[node] + next_node.dist
                priority_queue.push(next_node)
            }
        })
    }
}

function solution(N, road, K) {
    let graph = Array.from({ length: N + 1 }, () => []);
    let distances = new Array(N+1).fill(Infinity);
    let answer =0;

    road.map((route) => {
        graph[route[0]].push({
          node: route[1],
          dist: route[2],
        });
        graph[route[1]].push({
          node: route[0],
          dist: route[2],
        });
      });

    dijkstra(distances, graph)
    answer = distances.filter((dist) => dist <= K).length
    return answer
}

console.log(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))