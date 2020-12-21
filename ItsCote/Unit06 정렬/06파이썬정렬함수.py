array = [7,5,9,0,3,1,6,4,8]

result = sorted(array)
print(result)


print(array)
array.sort()
print(array)

array = [('바나나',2),('사과',1),('포도',4)]

def setting(data):
  return data[1]

result = sorted(array, key=setting)
print(result)