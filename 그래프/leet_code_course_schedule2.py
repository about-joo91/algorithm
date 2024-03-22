class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(cur_course: int) -> bool:
            if visited[cur_course] == -1:
                return False
            if visited[cur_course] == 1:
                return True

            visited[cur_course] = -1
            for next_course in graph[cur_course]:
                if not dfs(next_course):
                    return False

            visited[cur_course] = 1
            result.append(cur_course)
            
            return True
        
        graph = defaultdict(list)
        for post_course, pre_course in prerequisites:
            graph[pre_course].append(post_course)
        
        result = []
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []

        return result[::-1]




