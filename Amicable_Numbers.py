a=int(input())
b=int(input())
s=0
sum=0
for i in range(1,a):
    if a%i==0:
        s+=i
for i in range(1,b):
    if b%i==0:
        sum+=i
if s==b and sum==a:
    print('Amicable')
else:
    print('Not Amicable')