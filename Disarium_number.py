def disar_num(n):
    s=0
    j=1
    for i in str(n):
        s=(int(i))**j+s
        j+=1
    return s
n=int(input())
s=disar_num(n)
if s==n:
    print('True')
else:
    print('False')