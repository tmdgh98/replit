n = input()
x = int(n[1])
y = int(ord(n[0])-ord('a'))+1

dxy = [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]

count = 0;
for i in dxy :
  nx = x+i[0]
  ny = y+i[1]
  if(nx>0 and ny>0 and nx<9 and ny<9) :
    count+=1

print(count)