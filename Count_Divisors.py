l,r,k=map(int,input().split())
fc=0
s=0
for i in range(l,r+1):
    if i%k==0:
        fc+=1
        s+=1
print(fc)