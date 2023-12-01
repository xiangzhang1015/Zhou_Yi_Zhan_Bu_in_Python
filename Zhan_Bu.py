# Author--Xiang Zhang (xiang.alan.zhang@gmail.com)
# Date- Oct 08, 2023


import numpy as np
import pickle as pk

All_Gua_dic = pk.load(open('All_Gua_dic.pk', 'rb'))


def Si_Xiang(num):
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
    Tian = Si_Xiang(Tian)
    Di = Si_Xiang(Di)

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

print("本卦为", Ben_Gua)

Bian_Gua = []
Bian_Yao = []
Bu_Bian_Yao = []
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
        Bu_Bian_Yao.append(Yao)

len_Bian_Yao = len(Bian_Yao)

if len_Bian_Yao + len(Bu_Bian_Yao) !=6:
    raise ValueError('错误：总爻数不为6。')

if len_Bian_Yao >0:
    print("变卦:{}, \n变爻:{}".format(Bian_Gua, Bian_Yao))
else:
    print("无变卦")


def to_binary(li):
    return [i%2 for i in li]

####解卦############
# https://github.com/xiangzhang1015/Zhou_Yi_Zhan_Bu_in_Python

Ben_Gua_binary = to_binary(Ben_Gua)
Bian_Gua_binary = to_binary(Bian_Gua)
Ben_Gua_key = ''.join(map(str, Ben_Gua_binary))
Bian_Gua_key = ''.join(map(str, Bian_Gua_binary))



print( '\n本卦为 {}，'.format(All_Gua_dic[Ben_Gua_key][0]))
if len_Bian_Yao >0:
    print('变卦为 {}， \n'.format(All_Gua_dic[Bian_Gua_key][0]))

print('解卦结果如下：\n')

if len_Bian_Yao ==0:  # 本卦的卦辞
    print(
        '本卦的卦辞:', All_Gua_dic[Ben_Gua_key][0]
    )
elif len_Bian_Yao ==1:  #本卦变爻的爻辞
    print(
        '变爻是第{}爻。'.format(Bian_Yao),
        '本卦变爻的爻辞:', All_Gua_dic[Ben_Gua_key][1][Bian_Yao[0]-1]
    )
elif len_Bian_Yao ==2:  # 两个变爻的爻辞来判断凶吉，以上面的变爻为主。
    print(
        '变爻是第{}爻。'.format(Bian_Yao), '\n',
        '本卦变爻的爻辞:', All_Gua_dic[Ben_Gua_key][1][Bian_Yao[0] - 1], All_Gua_dic[Ben_Gua_key][1][Bian_Yao[1] - 1],
        '\n', '以上面的变爻为主, 即：', All_Gua_dic[Ben_Gua_key][1][Bian_Yao[1] - 1]
    )
elif len_Bian_Yao ==3:  # 用本卦和变卦的卦辞，以本卦的卦辞为主。
    print(
        '用本卦和变卦的卦辞，以本卦的卦辞为主。', '\n'
        '本卦的卦辞: {}'.format(All_Gua_dic[Ben_Gua_key][0]),
        '\n' '变卦的卦辞: {}'.format(All_Gua_dic[Bian_Gua_key][0])
    )

elif len_Bian_Yao == 4:  #变卦的两个不变爻的爻辞来判断吉凶，以下面的不变爻为主。
    print(
        '不变爻是第{}爻。'.format(Bu_Bian_Yao), '\n',
        '变卦的不变爻的爻辞:', All_Gua_dic[Bian_Gua_key][1][Bu_Bian_Yao[0]-1], All_Gua_dic[Bian_Gua_key][1][Bu_Bian_Yao[1]-1],
        '\n', '以上面的变爻为主, 即：', All_Gua_dic[Bian_Gua_key][1][Bu_Bian_Yao[0]-1]
    )

elif len_Bian_Yao == 5:  # 变卦的那一个不变爻的爻辞
    print(
        '不变爻是第{}爻。'.format(Bu_Bian_Yao), '\n',
        '变卦的那一个不变爻的爻辞:', All_Gua_dic[Bian_Gua_key][1][Bu_Bian_Yao[0]-1]
    )

elif len_Bian_Yao == 6:  #
    if sum(Bian_Gua_binary) == 6:  # 变卦为乾卦
        print(
            '六爻皆变，变卦为乾卦，看“用九”的爻辞。', '\n',
            '用九的爻辞为：', All_Gua_dic['111111'][1][-1]
        )
    elif sum(Bian_Gua_binary) == 0:  # 变卦为坤卦
        print(
            '六爻皆变，变卦为坤卦，看“用六”的爻辞。', '\n',
            '用六的爻辞为：', All_Gua_dic['000000'][1][-1]
        )
    else:  # 用变卦的卦辞
        print(
            '用变卦的卦辞, 为', All_Gua_dic[Bian_Gua_key][0]
        )

