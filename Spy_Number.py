n=int(input())
s=0
p=1
i=1
while i<=n:
    r=n%10
    n=n//10
    p=p*r
    s+=r
if p==s:
    print('Spy Number')
else:
    print('Not Spy Number')