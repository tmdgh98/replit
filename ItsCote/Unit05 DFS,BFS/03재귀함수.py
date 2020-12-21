def recursive_function(i):
  if i>=10:
    return
  print(i,"번쨰 재귀함수")
  i+=1
  recursive_function(i)

recursive_function(1)