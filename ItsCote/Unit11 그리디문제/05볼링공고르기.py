import sys
input = sys.stdin.readline
n, m = map(int,input().split())
data = list(map(int,input().split()))

count = 0
for i in range(len(data)):
  for j in range(i,len(data)):
    if data[i]==data[j]:
      continue
    count+=1

print(count)