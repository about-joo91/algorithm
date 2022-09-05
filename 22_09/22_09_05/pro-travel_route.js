function solution(tickets) {
    let answer = [];
    const result = [];
    const visited = []
    
    tickets.sort()
    let ticket_len = tickets.length;
    const dfs = (ticket, depth) =>{
        result.push(ticket)
        
        if (depth == ticket_len){
            answer = result;
            return true;
        }
        
        for (let i=0; i < ticket_len; i++){
            if(!visited[i] && tickets[i][0] == ticket){
                visited[i] = true;
                if(dfs(tickets[i][1], depth+1)) return true;
                visited[i] = false;
            }
        }
        result.pop()
        return false
    }
    dfs("ICN", 0)
    return answer;
}