# 水仙花數:自己的個十百位的三次方相加等於自己

print("水仙花數為:",end="")
for i in range(100,1000,1):
    x=i//100
    y=(i-x*100)//10
    z=i-x*100-y*10
    a=x**3+y**3+z**3
    if i==a :
        print(i,end=" ")


      