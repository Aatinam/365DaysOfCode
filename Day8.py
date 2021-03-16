
#Day 8 of 365 days of code
#Link for leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

#Problem Statement : Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
#return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or
# vertically. You may assume all four edges of the grid are all surrounded by water.

 
class Solution:
    def numIslands(self, grid) :
        count = 0;
        numRows = len(grid);
        numCols = len(grid[0]);
        visited = [[0 for col in range(numCols)] for row in range(numRows)];
        
        def dfs(row, col):
            if row < 0 or row >= numRows or col < 0 or col >= numCols or visited[row][col]:
                return;
            visited[row][col] = 1;
            if grid[row][col] == "0":
                return;
            else:
                dfs(row - 1,col);
                dfs(row + 1,col);
                dfs(row, col + 1);
                dfs(row, col - 1);
                
        for i in range(0, numRows):
            for j in range(0, numCols):
                if grid[i][j] == "1" and visited[i][j] != 1:
                    dfs(i, j);
                    count +=1;
        return count;
                    
            