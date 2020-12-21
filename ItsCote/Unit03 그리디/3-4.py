n, k = map(int, input().split())

count = 0
while n >= k:
  if(n%k==0):
    n /= k
  else:
    n-= 1
  count+= 1

count += (int)(n-1)
print(count)