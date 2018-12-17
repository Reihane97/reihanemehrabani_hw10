n=int(input("please enter first number:"))
m=int(input("please enter second number:"))
maximom=m if m<n else n
minimom=n if m<n else m
print("all common devisors are:")
for i in range(1,minimom+1):
    if maximom%i==0 and minimom%i==0:
        print(i)

        
    

    
