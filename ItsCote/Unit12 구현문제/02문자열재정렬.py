s = input()

alpha = []
num = 0

for i in s:
  if i.isupper() :
    alpha.append(i)
  else :
    num+= int(i)

alpha.sort()

alpha.append(str(num))

print(''.join(alpha))