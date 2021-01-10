#문자열 처리
str = "kdADcnCkla123asc";

#문자
for i in str:
  if i.isalpha():
    print(i, end=" ")
print()
#소문자
for i in str:
  if i.islower():
    print(i, end=" ")
print()
#대문자
for i in str:
  if i.isupper():
    print(i, end=" ")
print()
#숫자
for i in str:
  if i.isdigit():
    print(i, end=" ")

