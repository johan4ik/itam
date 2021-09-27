
k1,k2,ns=0,0,0
n=int(input())

for i in range(n):
  text=input().split()
  if text.count("True")+text.count("False")>=2: #если булевых переменных >=2
    if text[3]=="True": #если ласт элемент = тру
      k1+=1
    elif text[3]=="False": #если ласт элемент = фолс
      k2+=1
    else: # ни то ни другое
      ns+=1

  else:
    if text.count("True")==1 and text.count("False")==0:
      k1+=1
    else:
      k2+=1


print(k1,k2,ns)
