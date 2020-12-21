from collections import deque

r,c = map(int, input().split())

graph = []
for i in range(r):
  graph.append(list(map(int,input())))

def bfs(x,y):
  if graph[x][y]==0:
    queue = deque()
    queue.append((x,y))
    while queue:
      v = queue.popleft()
      x=v[0]
      y=v[1]
      if x>=0 and x<r and y>=0 and y<c and graph[x][y]==0 :
        graph[x][y]=1
        queue.append((x-1,y))
        queue.append((x,y-1))
        queue.append((x+1,y))
        queue.append((x,y+1))
    return True
  return False

count = 0
for i in range(len(graph)):
  for j in range(len(graph[i])):
    if bfs(i,j):
      count+=1
      
print(count)

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011100100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111100
# 00011111111000
# 00000000111000
# 11111111110011
# 11111111111111
# 11100011111111
# 11100011111111
# 11111111111111