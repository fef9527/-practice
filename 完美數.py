# 完美數 除了自己以外的因數相加等於自己

for i in range(1,10000):
    sum=0
    for j in range(1,i): 
        if i%j == 0 :
            sum=sum+j
    if sum==i:
        print("完美數為:",sum)
#~~


