n = input();

p = 0
a = 0
for i in range(len(n)//2) :
  p += int(n[i])

for i in range(len(n)//2, len(n)) :
  a += int(n[i])

if p == a :
  print("LUCKY")
else :
  print("READY")