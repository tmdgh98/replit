import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = list(map(int,input().split()))

array = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
  array[i][i]=0

for _ in range(m):
  a,b = list(map(int,input().split()))
  array[a][b] = 1
  array[b][a] = 1

k, x =list(map(int,input().split()))

for z in range(n+1):
  for i in range(n+1):
    for j in range(n+1):
      array[i][j] = min(array[i][j],array[z][j]+array[i][z])

answer = array[1][x]+array[x][k]

if answer>=INF:
  print(-1)
else:
  print(answer)

# 4 2
# 1 3
# 2 4
# 3 4

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5 