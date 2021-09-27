
n=int(input()) #количество строк
k1,k2=0,0  #k1-очный формат, k2-заочный формат
for i in range(n):
  lst = input().split()
  if lst[3]=="True":
    k1+=1
  else:
    k2+=1

print(k1,k2)
