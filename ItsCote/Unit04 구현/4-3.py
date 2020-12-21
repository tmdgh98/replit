r, c = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0]*c for _ in range(r)]

arr = []
for i in r :
  arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
d[x][y] = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dx[direction]
  if d[nx][ny] == 0 and arr[nx][ny] == 0 :
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    continue
  else:
    turn_time += 1
  
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if arr[nx][ny] == 0:
      x = nx
      y = ny
    else :
      break
    turn_time = 0

print(count)