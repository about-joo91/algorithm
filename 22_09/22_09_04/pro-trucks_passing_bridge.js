function solution(bridge_length, weight, truck_weights) {

    let answer = 0;
    let bridge = [];
    let bridge_weight = 0;
    while (truck_weights.length > 0){
        console.log(bridge)
        answer++;
        if (bridge.length == bridge_length){
            bridge_weight -= bridge.shift();
        }
        if (bridge_weight + truck_weights[0] > weight){
            bridge.push(0);
            continue;
        }
        let first_truck = truck_weights.shift()
        bridge.push(first_truck)
        bridge_weight += first_truck
    }
    answer += bridge_length;
    return answer;
}

console.log(solution(2,10,[7,4,5,6]))