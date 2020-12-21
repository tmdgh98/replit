numbers = input()
oneCount = 0
zeroCount = 0
number = int(numbers[0])
if number ==1:
  oneCount +=1
else:
  zeroCount +=1
for i in range(1,len(numbers)):
  n = int(numbers[i])
  if n==number:
    continue
  if n==1:
    number = n
    oneCount+=1
  else:
    number = n
    zeroCount+=1

print(min(zeroCount,oneCount))