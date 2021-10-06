
def summation(s):
    lst = [int(i) for i in s.split()] ##парсим в список в int
    for i in range(len(lst)): #отрицательные значения умн на -2
        if lst[i]<0:
            lst[i]*=-2

    return sum([i/max(lst) for i in lst]) #возвращаем сумму нормализованных чисел

s=input()
print(summation(s))
