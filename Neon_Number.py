n=int(input())
sq=n*n
sum=0
while sq>0:
    sum=sum+sq%10
    sq=sq//10
if n==sum:
    print('Neon Number')
else:
    print('Not Neon Number')