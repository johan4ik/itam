
text = input()
flag1, flag2 = False , False #флаги для нахождения большой буквы и первого символа после цифры

ind1, ind2 = 0, 0 #индексы этих элементов,чтобы найти интервал
for i in range(len(text)):
  if text[i].isupper() and flag1 == False: #если элемент Заглавный и флаг не помечен
    ind1 = i
    flag1 = True

  if text[i].isdigit() and flag2 == False and not(text[i+1].isdigit()): #если элемент - цифра и след элемент буква
    ind2 = i+1
    flag2 = True

print(text[ind1::ind2-ind1]) #через срез вывод начиная от заглавной буквы до конца с шагом = интервалу
