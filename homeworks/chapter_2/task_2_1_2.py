
def summation(sum):
    lst=[int(i) for i in sum.split()]
    sum=0
    Maximum=max(lst)
    for i in lst:
        if i<0:
            i*=-1
            i*=2

        i /= Maximum
        sum+=i

    return sum


sum=input()
x=summation(sum)
x=float('{:.3f}'.format(x))
print(x)
