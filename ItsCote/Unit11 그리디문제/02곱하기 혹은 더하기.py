numbers = input()
array = []
for i in range(len(numbers)):
  array.append(int(numbers[i]))

array.sort()

result = 1
for i in array:
  if i==0:
    continue
  result *= i

print(result)