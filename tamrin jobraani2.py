def todecimal(n,k):
    sum1=0
    c=1
    while(n>0):
        r=n%10
        sum1=sum1+r*c
        c*=k
        n//=10
    return sum1
def from10tootherbase(n,k):
    sum2=0
    d=1
    while(n>0):
        r=n%k
        sum2+=r*d
        d*=10
        n//=k
    return sum2

n=int(input("please enter a number in a base smaller than 10:"))
k=int(input("please enter the base you want to convert:"))
todecimal(n,k)
print(from10tootherbase(n,k))
        
        
    
    

