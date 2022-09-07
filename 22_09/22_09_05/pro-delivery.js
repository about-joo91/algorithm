const dijkstra = (distances,mileages, graph, k) => {
    let priority_queue =[];
    priority_queue.push({node : 1, dist : 0, mileage : 0});
    distances[1] = 0;
    mileages[1] = 0;
    let k_mileage  =[];

    while (priority_queue.length !==0 ){
        priority_queue.sort((a, b) => a.dist - b.dist)
        const node = priority_queue.shift().node;
        graph[node].forEach((next_node) => {     
            if(distances[next_node.node] >= distances[node] + next_node.dist){
              
                distances[next_node.node] = distances[node] + next_node.dist                
                mileages[next_node.node] = mileages[node]  + next_node.mileage 
                priority_queue.push(next_node)
                if (next_node.node == k){
                  k_mileage.push([distances[k], mileages[k]])
                }
            }
        })
    }
  k_mileage = k_mileage.filter(element => element[0] === distances[k])
  let answer = k_mileage.reduce((pre, cur) => {
    return pre[1] > cur[1] ? pre: cur;
  })
  return answer
}

function solution(n, k, paths) {
    let graph = Array.from({ length: n + 1 }, () => []);
    let distances = new Array(n+1).fill(Infinity);
    let mileages = new Array(n+1).fill(-Infinity)
    let answer;

    paths.map((route) => {
        graph[route[0]].push({
          node: route[1],
          dist: route[2],
          mileage: route[3]
        });
        graph[route[1]].push({
          node: route[0],
          dist: route[2],
          mileage: route[3]
        });
      });

    answer = dijkstra(distances,mileages, graph,k)
    return answer
}

console.log(solution(5,4,[[1, 5, 1, 1], [1, 2, 4, 3], [1, 3, 3, 2], [2, 5, 2, 1], [2, 4, 2, 3], [3, 4, 2, 2]]))
// class Heap {
//   constructor() {
//     this.heap = [];
//   }
//   getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1
//   getRightChildIndex = (parentIndex) => parentIndex * 2 + 2
//   getParentIndex = (childIndex) => Math.floor((childIndex - 1) / 2)

//   peek = () => this.heap[0]

//   insert = (priority, value) => { // 우선순위를 비교하기 위해서 priority와 value 로 받는다.
//     const node = { priority, value } // 객체로 node 를 만들고
//     this.heap.push(node) // push 한다.
//     this.heapifyUp() // 배열에 가장 끝에 넣고, 다시 min heap 의 형태를 갖추도록 한다.
//   }

//   heapifyUp = () => {
//     let curIndex = this.heap.length - 1 // 계속해서 변하는 index 값
//     const lastInsertedNode = this.heap[curIndex]

//     // 루트노드가 되기 전까지
//     while (curIndex > 0) {
//       const parentIndex = this.getParentIndex(curIndex)

//       // 부모 노드의 key 값이 마지막에 삽입된 노드의 키 값 보다 크다면
//       // 부모의 자리를 계속해서 아래로 내린다.
//       if (this.heap[parentIndex].priority > lastInsertedNode.priority) {
//         this.heap[curIndex] = this.heap[parentIndex]
//         curIndex = parentIndex
//       } else break
//     }

//     // break 를 만나서 자신의 자리를 찾은 상황
//     // 마지막에 찾아진 곳이 가장 나중에 들어온 노드가 들어갈 자리다.
//     this.heap[curIndex] = lastInsertedNode
//   }

//   pop = () => {
//     const count = this.heap.length
//     const rootNode = this.heap[0]

//     if (count <= 0) return undefined
//     if (count === 1) this.heap = []
//     else {
//       this.heap[0] = this.heap.pop() // 끝에 있는 노드를 부모로 만들고
//       this.heapifyDown() // 다시 min heap 의 형태를 갖추도록 한다.
//     }

//     return rootNode
//   }
//   heapifyDown = () => {
//     let index = 0
//     const count = this.heap.length
//     const rootNode = this.heap[index]

//     // 계속해서 left child 가 있을 때 까지 검사한다.
//     while (this.getLeftChildIndex(index) < count) {
//       const leftChildIndex = this.getLeftChildIndex(index)
//       const rightChildIndex = this.getRightChildIndex(index)

//       // 왼쪽, 오른쪽 중에 더 작은 노드를 찾는다
//       // rightChild 가 있다면 key의 값을 비교해서 더 작은 값을 찾는다.
//       // 없다면 leftChild 가 더 작은 값을 가지는 인덱스가 된다.
//       const smallerChildIndex =
//         rightChildIndex < count && this.heap[rightChildIndex].key < this.heap[leftChildIndex].key
//           ? rightChildIndex
//           : leftChildIndex

//       // 자식 노드의 키 값이 루트노드보다 작다면 위로 끌어올린다.
//       if (this.heap[smallerChildIndex].key <= rootNode.key) {
//         this.heap[index] = this.heap[smallerChildIndex]
//         index = smallerChildIndex
//       } else break
//     }

//     this.heap[index] = rootNode
//   }
//   }

// class PriorityQueue extends Heap {
//   constructor(){
//     super()
//   }

//   enqueue = (priority, value) => this.insert(priority, value)
//   dequeue = () => this.pop()
//   isEmpty = () => this.heap.length <= 0
// }
// console.log(solution(6,4, [[1, 5, 1, 1], [1, 2, 4, 3], [1, 3, 3, 2], [2, 5, 2, 1], [2, 4, 2, 3], [3, 4, 2, 2] ]))


// const priorityQueue = new PriorityQueue();



// priorityQueue.enqueue(5, {node:1, dist:5, mileage:3})
// priorityQueue.enqueue(6, {node:1, dist:5, mileage:3})
// priorityQueue.enqueue(2, {node:1, dist:5, mileage:3})
// priorityQueue.enqueue(4, {node:1, dist:5, mileage:3})
// priorityQueue.enqueue(3, {node:1, dist:5, mileage:3})
// priorityQueue.enqueue(1, {node:1, dist:5, mileage:3})


// console.log(priorityQueue.isEmpty())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.dequeue())
// console.log(priorityQueue.isEmpty())
