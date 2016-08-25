import random
def gcode(P,M):#生成编码，P为样本数，M为编码长度
    a=[]
    for i in range(P):#样本数
        a.append([])
        for j in range(M):#编码长度
            a[i].append(str(random.randint(0,1)))
    return a   #返回P*M的列表


if __name__ == '__main__':
    print(gcode(5,10))
