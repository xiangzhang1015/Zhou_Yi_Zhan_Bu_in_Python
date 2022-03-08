import numpy as np

def update(num):
    Yu = num%4
    if Yu==0:
        Yu = 4
    return num-Yu

Da_Yan = 50
Bian_Hua = 49


def Bian(Bian_hua):
    rate = np.random.randint(1, Bian_hua)
    # Fen Tian Di
    Tian = rate
    Di = Bian_hua - Tian

    # Ding San Cai
    Di = Di -1
    Ren = 1

    # Chu Si Xiang
    Tian = update(Tian)
    Di = update(Di)

    # Gui Hun Dun
    Bian_hua = Tian + Di
    return Bian_hua

def San_Bian(Da_Yan):
    Bian_hua = Da_Yan
    for i in range(3):
        Bian_hua = Bian(Bian_hua)
    return Bian_hua

Ben_Gua = []
for j in range(6):
    Yao = San_Bian(Bian_Hua)/4
    Ben_Gua.append(int(Yao))
print("Ben Gua", Ben_Gua)

Bian_Gua = []
Bian_Yao = []
for Yao in range(1,7):
    i = Ben_Gua[Yao-1]
    if i==6:
        Bian_Gua.append(7)
        Bian_Yao.append(Yao)
    elif i ==9:
        Bian_Gua.append(8)
        Bian_Yao.append(Yao)
    else:
        Bian_Gua.append(i)
        
if len(Bian_Yao) >0:
    print("Bian Gua:{}, Bian Yao:{}".format(Bian_Gua, Bian_Yao))
else:
    print("No Bian Gua")


