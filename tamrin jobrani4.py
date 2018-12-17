x1=int(input("enter first dot x1 "))
y1=int(input("enter first dot y1"))
x2=int(input("enter second dot x2"))
y2=int(input("enter second dot y2 "))
x3=int(input("enter third dot x3"))
y3=int(input("enter third dot y3"))

length1=(((x2-x1)**2)+((y2-y1)**2))**0.5
length2=(((x3-x2)**2)+((y3-y2)**2))**0.5
length3=(((x3-x1)**2)+((y3-y1)**2))**0.5
print(length1)
print(length2)
print(length3)
p=(length1+length2+length3)/2
area=((p*(p-length1)*(p-length2)*(p-length3)))**0.5
perime=length1+length2+length3
print("area: "+str(area)+"  perime:"+str(perime))
