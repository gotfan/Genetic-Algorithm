import itertools
import bisect
import random
def sel(L):
    M=list(itertools.accumulate(L))#生成数列的累加列表
    print(M)#打印累加数列
    total=M[-1]#累加数列的最大值
    p=bisect.bisect(M,random.randint(0,total))
    if p==len(M):
        p=p-1
    return p   #返回第几组样本被选中，位置为0到（样本数-1）


if __name__ == '__main__':
    L=[10,10,9,9]
    print(sel(L))
