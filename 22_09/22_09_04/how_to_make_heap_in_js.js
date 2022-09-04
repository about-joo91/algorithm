class Heap {
    constructor() {
      this.heap = [ null ];
    }
    getMin() {
        return this.heap[1] ? this.heap[1] : null;
    }
    size() {
        return this.heap.length - 1;
    }

    heappush(value) {
        this.heap.push(value);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        // 최소힙이므로 부모노드가 제일 작아야 한다. 즉 부모노드가 현재노드보다 큰 지 검사하며 반복한다.
        while(curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
          [ this.heap[parIdx], this.heap[curIdx] ] = [ this.heap[curIdx], this.heap[parIdx] ];
          // 구조분해 할당을 이용해 부모와 자식을 swap 한다. 따로 함수로 빼주어 작성해도 좋다.
          curIdx = parIdx;
          parIdx = (curIdx / 2) >> 0;
        }
      }
      heappop() {
        const min = this.heap[1];	// 배열 첫 원소를 비워두므로 root는 heap[1]에 항상 위치한다.
        if(this.heap.length <= 2) this.heap = [ null ];
        else this.heap[1] = this.heap.pop();
        // 배열 마지막 원소를 root 위치에 먼저 배치하는 과정이다.
        // if-else로 분기되는 이유는 추후 heap이 비었는지 아닌지 확인하기 위해 size 체크 함수를 만들때 -1을 통해 0을 만들어주기 때문.
        
        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1;
        
        if(!this.heap[leftIdx]) return min;
        // 왼쪽 자식이 없다는 것은 오른쪽 자식도 없는, 즉 루트만 있는 상태이므로 바로 반환!
        if(!this.heap[rightIdx]) {
          if(this.heap[leftIdx] < this.heap[curIdx]) {
            [ this.heap[leftIdx], this.heap[curIdx] ] = [ this.heap[curIdx], this.heap[leftIdx] ];
            // 오른쪽 자식이 없다면 왼쪽 자식하나만 있다는 것을 의미한다.
          }
          return min;
        }
        
        // 위에 조건에 걸리지 않는 경우 왼쪽과 오른쪽 자식이 모두 있는 경우이다.
        // 따라서 현재 노드가 왼쪽 또는 오른쪽 보다 큰 지 작은지를 검사하며 반복한다.
        while(this.heap[leftIdx] < this.heap[curIdx] || this.heap[rightIdx] < this.heap[curIdx]) {
          // 왼쪽과 오른쪽 자식 중에 더 작은 값과 현재 노드를 교체하면 된다.
          const minIdx = this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
          [ this.heap[minIdx], this.heap[curIdx] ] = [ this.heap[curIdx], this.heap[minIdx] ];
          curIdx = minIdx;
          leftIdx = curIdx * 2;
          rightIdx = curIdx * 2 + 1;
        }
        
        return min;
      }
    }
    

let heap = new Heap();

heap.heappush(7)
heap.heappush(1)
heap.heappush(5)

while(heap.size() >0){
    console.log(heap.heappop())
}
