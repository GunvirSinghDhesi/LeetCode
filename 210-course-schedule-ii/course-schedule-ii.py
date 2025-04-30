class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        result = []

        def dfs(course):
            if visited[course] == 1:
                return False  # cycle
            if visited[course] == 2:
                return True   # already processed

            visited[course] = 1  # mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2  # mark as visited
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []  # cycle detected

        return result[::-1]  # reverse to get correct order