import sys
input = sys.stdin.readline

n = int(input())
array = []
array = list(map(int,input().split()))

array.sort()

count = 0
member = 0
for i in array:
  member += 1
  if i <= member:
    member=0
    count+=1

print(count)

# 5
# 2 3 1 2 2