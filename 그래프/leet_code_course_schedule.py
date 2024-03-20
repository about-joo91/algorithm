class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for post_course, prev_course in prerequisites:
            graph[prev_course].append(post_course)
            in_degree[post_course] +=1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        result = []
        while queue:
            cur_course = queue.popleft()
            result.append(cur_course)
            for next_course in graph[cur_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return len(result) == numCourses
