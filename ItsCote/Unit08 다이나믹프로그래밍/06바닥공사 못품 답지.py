#정수 n을 입력받기
n = int(input())

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
array = [0]*1001

#다이나믹 프로그래밍 진행(보텀업)
array[0]=1
array[1]=3
for i in range(2,n):
  array[i] = array[i-1]+array[i-2]*2

#계산된 결과 출력
print(array[n-1])