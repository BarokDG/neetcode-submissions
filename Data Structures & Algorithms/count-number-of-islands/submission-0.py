class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        row_len, col_len = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = collections.deque([(r, c)])
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= row_len or
                        nc >= col_len or grid[nr][nc] == "0"
                    ):
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands