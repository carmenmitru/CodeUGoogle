class Tile:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    def isSafe(self, i, j, visited):
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
             
    def DFS(self, i, j, visited):
        #Direction arrays
        rowNbr = [-1,0,-1,0];
        colNbr = [0,1,0,-1];
         
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recursion  al connected neighbours
        for k in range(4):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)
 
 
     def countIslands(self):
        # Make a bool array to mark visited cells.Initially all cells are unvisited
        visited = [[0 for j in range(self.COL)]for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == 0 and self.graph[i][j] == True:
                    self.DFS(i, j, visited)
                    count += 1
 
        return count
 
 
graph = [
            [0, 1, 0, 1],
            [1, 1,0, 0],
            [0, 0, 1,0],
            [0, 0, 1,0]
        ]
 
 
row = len(graph)
col = len(graph[0])
 
g= Tile(row,col,grapf)
 
print "Number of islands is :"
print g.countIslands()
