n = int(input())
arr = list(map(int, input().split()))
m = int(input())
sArr = list(map(int,input().split()))

def search(arr, target, start, end):
  if start>end:
    return False
  mid = (start+end)//2
  if arr[mid] == target:
    return True
  elif arr[mid] > target:
    return search(arr,target,start,mid-1)
  else:
    return search(arr,target,mid+1,end)


arr.sort()
print(arr)
for i in sArr:
  if search(arr,i,0,n-1):
    print("yes")
  else:
    print("no")

# 5
# 8 3 7 9 2
# 3 
# 5 7 9