function solution(n, k, paths) {
    const routes = Array.from({ length:n+1}, () => []);
    const distances = new Array(n+1).fill(Infinity);
    const mileages = new Array(n+1).fill(-Infinity);
    let answer;

    // path의 양쪽방향으로 graph를 그려준다.
    paths.map((route) => {
        routes[route[0]].push({
            node: route[1],
            dist: route[2],
            mileage: route[3]
        });
        routes[route[1]].push({
            node: route[0],
            dist: route[2],
            mileage: route[3]
        });
    });

    //다익스트라 계산 부분을 함수로 분리
    answer = dijkstra(distances, mileages,routes, k);
    return answer;
};


const dijkstra = (distances, mileages, routes, k) => {
    let priorityQueue = new PriorityQueue();
    // 1에서 출발하므로 1로 queue의 시작값을 설정해주고
    // distances의 1과 mileages의 1도 0으로 초기값 설정을 해준다.
    priorityQueue.enqueue( 0, {
        node:1,
        dist:0,
        mileage:0
    });
    distances[1] = 0;
    mileages[1] = 0;
    let mileagesOfK = [];

    // 프라이머리 큐가 비어있다면 종료
    while (!priorityQueue.isEmpty()){

        // 커스텀 프라머리큐의 dequeue를 통해서 거리가 제일 짧은 노드를 가져온다.
        const dequeuedValue = priorityQueue.dequeue().value;
        const node = dequeuedValue.node;
        // 현재 공항과 연결된 모든 공항들의 거리를 최소값으로 업데이트 해준다.
        // 그 과정에서 마일리지도 최신값으로 업데이트를 해준다.
        routes[node].forEach((nextNode) => {
            // 기존의 distances 값과 비교하여 더 작다면 distances의 값을 변경해준다.
            if(distances[nextNode.node] >= distances[node] + nextNode.dist){
                distances[nextNode.node] = distances[node] + nextNode.dist;
                mileages[nextNode.node] = mileages[node] + nextNode.mileage;
                priorityQueue.enqueue(nextNode.dist, nextNode);
                // k 공항의 최소값이 되었을 때의 마일리지 값을 
                if (nextNode.node === k){
                    mileagesOfK.push([distances[k], mileages[k]]);
                }
            }
        })
    }
    // 거리가 최소값이 아닐 때 마일리지 값이 들어갔을 수도 있기 때문에
    // filter를 통해 거르고 reduce를 통해
    // 마일리지의 최대값을 반환해준다.
    mileagesOfK = mileagesOfK.filter(element => element[0] === distances[k]);
    let answer = mileagesOfK.reduce((pre, cur) => {
        return pre[1] > cur[1] ? pre : cur;
    })
    return answer;
}

class Heap {
    constructor(){
        this.heap = [];
    }

    getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1;
    getRightChildIndex = (parentIndex) => parentIndex * 2 + 2;
    getParentIndex = (childIndex) => Math.floor((childIndex - 1) / 2);

    // 우선순위 비교를 위해 priority 값을 받아준다.
    insert = (priority, value) => {
        // priority 와 value값을 객체로 만들어줌
        const node = {priority, value};
        this.heap.push(node);
        this.heapifyUp();
    }

    // 큐에 추가된 이후 heapify하기 위한 함수
    heapifyUp = () => {
        // 현재 노드값을 저장
        // 계속 업데이트 되기 때문에 let으로 저장
        let curIndex = this.heap.length -1;
        const lastInsertedNode = this.heap[curIndex];

        while (curIndex > 0){
            const parentIndex = this.getParentIndex(curIndex);

            // 삽입된 값의 인덱스를 업데이트 해준다.
            if (this.heap[parentIndex].priority > lastInsertedNode.priority){
                this.heap[curIndex] = this.heap[parentIndex];
                curIndex = parentIndex;
            }else break
        }

        this.heap[curIndex] = lastInsertedNode;
    }

    pop = () => {
        const count = this.heap.length;
        const rootNode = this.heap[0];

        if(count <= 0) return undefined;
        if(count === 1) this.heap = [];
        // 끝 노드를 헤드에 넣고
        // 미리 담아둔 헤드값을 리턴하고
        // 다시 위치를 조정해준다.
        else{
            this.heap[0] = this.heap.pop();
            this.heapifyDown();
        }
        return rootNode;
    }

    // 큐에서 값을 팝한 이후 heapify하기 위한 함수
    heapifyDown = () => {
        let index = 0;
        const count = this.heap.length;
        const rootNode = this.heap[index];

        // 왼쪽 노드가 있을 때까지 반복
        while (this.getLeftChildIndex(index) < count){
            const leftChildIndex = this.getLeftChildIndex(index);
            const rightChildIndex = this.getRightChildIndex(index);

            // 오른쪽과 왼쪽을 비교하여 작은 값을 구한다.
            const smallerChildIndex = rightChildIndex < count && this.heap[rightChildIndex].priority < this.heap[leftChildIndex].priority
            ? rightChildIndex : leftChildIndex;


            // 루트노드가 자식노드보다 크다면 아래로 내린다.
            if (this.heap[smallerChildIndex].priority <= rootNode.priority){
                this.heap[index] = this.heap[smallerChildIndex];
                index = smallerChildIndex;
            }else break;
        }

        this.heap[index] = rootNode;
    }
}

class PriorityQueue extends Heap{
    constructor(){
        super();
    }

    enqueue = (priority, value) => this.insert(priority, value);
    dequeue = () => this.pop();
    isEmpty = () => this.heap.length <=0;
}
