lst = [int(i) for i in input().split()] #создаем список целых чисел
minus,upper_eight,even=0,0,0 #счетчики
for i in lst: #пробегаем по списку
  if i<0:
    minus+=1
  if i>8:
    upper_eight+=1
  if i%2==0:
    even+=1
print(minus,upper_eight,even) # выводим количества
