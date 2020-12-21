from collections import deque

r,c = map(int, input().split())
graph=[]
for i in range(r):
  graph.append(list(map(int,input())))

def bfs(x,y):
  i = 0
  queue = deque()
  queue.append((x,y,1))
  while queue:
    v = queue.popleft()
    x = v[0]
    y = v[1]
    i = v[2]
    if x==r-1 and y==c-1 :
      return i
    if x>=0 and x<r and y>=0 and y<c and graph[x][y]==1 :
      graph[x][y]=0
      queue.append((x+1,y,i+1))
      queue.append((x,y+1,i+1))
      queue.append((x-1,y,i+1))
      queue.append((x,y-1,i+1))
      

print(bfs(0,0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111