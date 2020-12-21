n = int(input())
arr = []
for i in range(n):
  data = input().split()
  arr.append((data[0],int(data[1])))

def setting(d):
  return d[1]

array = sorted(arr, key=setting)
arr = sorted(arr, key=lambda student: student[1])

print(array)
print(arr)

# 3
# 홍길동 95
# 이순신 77
# 곽승호 100