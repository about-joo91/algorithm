function solution(map3d) {
    let start = [];
    let limitDepth = map3d.length;
    let limitRow = map3d[0].length;
    let limitColumn = map3d[0][0].length;
    const visited = new Array(limitDepth);


    // start 지점을 찾으면서 동시에 visited 배열을 초기화 해준다.
    // depth -> row -> column 순으로 순회를 해준다.
    for (let i = 0; i < limitDepth; i++){
        visited[i] = new Array(limitRow);
        for (let j = 0; j < limitRow; j++){
            visited[i][j] = new Array(limitColumn).fill(0);
            for (let k = 0; k < limitColumn; k++){
                if(map3d[i][j][k] === 'S'){
                    // 시작점과 거리를 지정해줌
                    start = [i, j, k, 0];
                }
            }
        }
    }
    return bfs(start, map3d, limitDepth, limitRow, limitColumn, visited);

};

const bfs = (start, map3d, limitDepth, limitRow, limitColumn, visited) => {
    const queue = [];
    // 6가지 방향을 미리 지정해준다 순서대로
    // 위 아래 앞 뒤 좌 우
    const dDepth = [-1, 1, 0, 0, 0, 0];
    const dRow = [0, 0, 1, -1, 0, 0];
    const dColumn = [0, 0, 0, 0, 1, -1];
    // 받아온 출발 지점을 queue에 넣어주고
    // visited에 방문표시를 해준다.
    queue.push(start);
    visited[start[0]][start[1]][start[2]] = 1;

    //queue가 빌 때까지 while문을 반복
    while (queue.length){
        // 현재 깊이, 행, 열, 거리를 뽑아준다.
        let [curDepth, curRow, curColumn, dist] = queue.shift();

        for (let i = 0; i < 6; i++){
            // 6방향에 대한 다음 값들을 선언
            let nextDepth = curDepth + dDepth[i];
            let nextRow = curRow + dRow[i];
            let nextColumn = curColumn + dColumn[i];

            // 다음 값들이 0과 limit값 사이에 있는지 검사하여 바른 길인지 확인한다.
            // 바른 길 -> 배열의 길이를 초과하지 않는지 검사
            if (isRightWay(nextDepth, nextRow, nextColumn, limitDepth, limitRow, limitColumn)){
                // 만약 다음 이동할 값이 'E'라면 끝나는 값이므로 확인후 dist+1을 반환해준다.
                if (isEnd(nextDepth, nextRow, nextColumn, map3d)){
                    return dist+1;
                }
                // 끝나는 값이 아니라면 이동이 가능한지 검사를 한다.
                // 검사를 통과한다면 visited의 값을 1로 바꿔 방문처리를 하고
                // 큐에 넣어 이동할 수 있도록 해준다.
                if (canMove(nextDepth,nextRow,nextColumn, visited,map3d)){
                    visited[nextDepth][nextRow][nextColumn] =1;
                    queue.push([nextDepth, nextRow, nextColumn,dist+1]);
                }
            }
        }
    }
    // E까지 닿을 수 없다면 -1 리턴
    return -1;
};

// 다음에 이동할 값은 주어진 배열의 길이 안에 있어야 한다.
const isRightWay = (nextDepth, nextRow, nextColumn, limitDepth, limitRow, limitColumn) => {

    if (0 <= nextDepth && nextDepth < limitDepth && 0<= nextRow && nextRow < limitRow && 0<= nextColumn && nextColumn < limitColumn) {
        return true
    } return false
};

// 다음 이동장소가 E라면 도착지점에 닿은 것이다.
const isEnd = (nextDepth, nextRow, nextColumn, map3d) => {
    let pathValue = map3d[nextDepth][nextRow][nextColumn];
    if (pathValue === "E") {
        return true
    } return false
};

// visited의 값이 0이라면 방문한 적이 없는 것이고
// map3d의 값이 "O"여야 이동할 수 있다.
const canMove = (nextDepth, nextRow, nextColumn,visited, map3d) => {

    if (visited[nextDepth][nextRow][nextColumn] === 0 && map3d[nextDepth][nextRow][nextColumn] === "O") {
        return true
    } return false
};
