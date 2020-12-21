# 정수 N을 입력받기
n = int(input())
#모든 식량 정보 입력받기
array = list(map(int, input().split(" ")))

#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
a = [0]*100

#다이나믹 프로그래밍 진행(보텀업)
a[0]= array[0]
a[1] = max(array[0],array[1])
for i in range(2,n):
  a[i] = max(a[i-1], a[i-2]+array[i])

#계산된 결과
print(a[n-1])