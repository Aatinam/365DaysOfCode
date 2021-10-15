#Day 21 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/walls-and-gates/

#Problem Statement : You are given an m x n grid rooms initialized with these three possible values.
#-1 A wall or an obstacle.
#0 A gate.
#INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that 
#the distance to a gate is less than 2147483647.
#Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


from collections import deque;

class Solution:
    def bfs(self, rooms, i, j):
        numRows = len(rooms);
        numColumns = len(rooms[0]);
        GATE = 0;
        WALL = -1;
        INF = 2147483647
        visited = [[0 for col in range(numColumns)] for row in range(numRows)]
        queue = deque();
        queue.append([i,j, 0]);
        visited[i][j] = 1;
        
        while(len(queue) > 0):
            indices = queue.popleft();
            row = indices[0];
            column = indices[1];
            degree = indices[2];
            if rooms[row][column] == GATE:
                ### gate found return something
                return degree;
                
            if column+1 < numColumns and rooms[row][column+1] != WALL and not visited[row][column+1]:
                visited[row][column+1] = 1;
                queue.append([row, column+1, degree+1])
            if column-1 > 0 and rooms[row][column-1] != WALL and not visited[row][column-1]:
                visited[row][column-1] = 1;
                queue.append([row, column-1, degree+1])
            if row+1 < numRows and rooms[row+1][column] != WALL and not visited[row+1][column]:
                visited[row+1][column] = 1;
                queue.append([row+1, column, degree+1])
            if row-1 > 0 and rooms[row-1][column] != WALL and not visited[row-1][column]:
                visited[row-1][column] = 1;
                queue.append([row-1, column, degree+1])
                
        return INF;
            
        
        
        
        
        
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m = len(rooms)
        n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] != -1 and rooms[i][j] != 0:
                    rooms[i][j] = self.bfs(rooms, i, j)
                    

if __name__ == "__main__":
    sol = Solution();
    sol.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
                
            