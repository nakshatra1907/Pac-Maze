from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self,grid):
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        def cango(x,y,n,m):
            return 0<=x<n and 0<=y<m
                
        def traverse(x,y,n,m):
            dir=[]
            if cango(x+1,y,n,m) and vis[x+1][y]==0 and pacmaze[x+1][y]!=1:
                dir.append((x+1,y))
            if cango(x-1,y,n,m) and vis[x-1][y]==0 and pacmaze[x-1][y]!=1:
                dir.append((x-1,y))
            if cango(x,y+1,n,m) and vis[x][y+1]==0 and pacmaze[x][y+1]!=1:
                dir.append((x,y+1))
            if cango(x,y-1,n,m) and vis[x][y-1]==0 and pacmaze[x][y-1]!=1:
                dir.append((x,y-1))
            nextcells.push(dir)
        pacmaze=self.navigator_maze
        n,m=len(pacmaze),len(pacmaze[0])
        
        vis=[[0 for j in range(m)] for i in range(n)]
        x,y=start[0],start[1]
        ex,ey=end[0],end[1]
        path=Stack()
        nextcells=Stack()
        path.push(start)
        traverse(x,y,n,m)
        vis[x][y]=1
        if pacmaze[x][y]==1 or pacmaze[ex][ey]==1:
            raise PathNotFoundException
        
        while path.top()!=end:
            
            if nextcells.top():
                c=nextcells.top()[-1]
                nextcells.top().pop()
                traverse(c[0],c[1],n,m)
                path.push(c)
                vis[c[0]][c[1]]=1
            else:
                vis[path.top()[0]][path.top()[1]]=0
                path.popit()
                nextcells.popit()
            if len(nextcells.top())==0 and path.top()==start:
                raise PathNotFoundException
        return path.givepath()
