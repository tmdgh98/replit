import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))

array.sort()

target = 1
for x in array:
  #만들 수 없는 금액을 찾았을 때 반복 종료
  if target < x:
    break
  target += x

#만들수 없는 금액 출력
print(target)
