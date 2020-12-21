# 정수 입력받기
n, target = list(map(int,input().split()))

# n개의 화폐단위 정보 입력받기
array = []
for i in range(n):
  array.append(int(input()))
array.sort()

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
ans = [10001]*(target+1)

# 다이나믹 프로그래밍 진행(보텀업)
ans[0] = 0
for i in range(n):
  for j in range(array[i],target+1):
    if ans[j-array[i]]!=10001:
      ans[j] = min(ans[j],ans[j-array[i]]+1)

#계산된 결과 출력
if ans[target]!=10001:
  print(ans[target])
else:
  print(-1)

