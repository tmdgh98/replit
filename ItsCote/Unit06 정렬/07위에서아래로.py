n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

arr = sorted(array, reverse=True)
array.sort(reverse=True)

print(arr)
print(array)