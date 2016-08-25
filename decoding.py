def dcode(L,P,M):#解码,P为样本数，M为编码长度
    Z=[]
    for i in range(P):
        A=L[i]
        A1=A[:M]
        A1=''.join(A1)
        a1=int(A1, 2)
        A2 = A[M:]
        A2 = ''.join(A2)
        a2 = int(A2, 2)
        Z.append(a1+(a2/100))
    return Z    #返回了解码后的值a1.a2



if __name__ == '__main__':
    T = [['1', '0', '0', '1'], ['1', '1', '0', '0']]
    print(dcode(T,2,2))
