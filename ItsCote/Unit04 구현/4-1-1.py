n = int( input())
data = list(input().split())

cmd = ['L','R','U','D']
dx = [-1,1,0,0]
dy = [0,0,-1,1]

x,y = 1,1

for i in data:
  for j in range(len(cmd)) :
    if i==cmd[j] :
      nx = x+dx[j]
      ny = y+dy[j]
      break
  if nx<1 or ny<1 or nx>n or ny>n :
    continue
  x, y = nx, ny

print(x,y)