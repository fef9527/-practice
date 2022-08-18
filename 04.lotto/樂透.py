#樂透號碼生成 隨機抽出六個不重複號碼
import random
lotto =[]
num49 = [i for i in range(1,50)]
# print(num48)
for i in range(6):
#n1 = random.randint(1,48)
    n1 = random.choice(num49)
    lotto.append(n1)
    lotto.sort()
    num49.remove(n1)
    sp = random.choice(num49)

print("中獎號碼",lotto)
print("特別號:",sp)
