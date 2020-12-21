n, m = map(int, input().split())

array = list(map(int, input().split()))

def search(array, target, start, end):
  mid = (start+end)//2
  if start > end:
    return mid
  sum = 0
  for i in array:
    if i-mid>0:
      sum += i-mid
  if sum==target:
    return mid
  elif sum>target:
    return search(array, target, mid+1, end)
  else:
    return search(array, target, start, mid-1)

print(search(array, m , 10, max(array)))

# 4 6
# 19 15 10 17  

