lst=[int(i) for i in input().split()] #генерируем список
max=lst[0] # изначально в min и max хранится нулевой элемент списка
min=lst[0]

for i in range(1,len(lst)): #цикл от 1 элемента
    if lst[i]>max:
        max=lst[i]
    if lst[i]<min:
        min=lst[i]

print(min,max)
