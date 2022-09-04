function solution(bridge_length, weight, truck_weights) {
    let bridge_weight = 0;
    let bridge = [];
    let answer = 0;
    while (truck_weights.length > 0) {
        answer ++;
        if (bridge.length == bridge_length){
            bridge_weight -= bridge.shift();
        }
        if (weight < truck_weights[0] + bridge_weight){
            bridge.push(0);
            continue;
        }
        let first_truck = truck_weights.shift();
        bridge.push(first_truck);
        bridge_weight += first_truck;
    }
    answer += bridge_length
    return answer;
}