#coding:utf-8
import numpy as np

class Tem2Rgb:
    def __init__(self,path):
        self.__data = np.load(path)

    def getrgbbytem(self,tem,deg=2): #deg 2 or 10 色温范围1000-40000 跨度100
        if tem<1000:  tem = 1000
        if tem>40000: tem = 40000
        ind = int((tem - 1000)/100)
        if deg==10: ad = 1
        else:       ad = 0
        print ind*2+ad
        return self.__data[ind*2+ad,:]

    def getrgb(self,tem,temrange):
        scale = (temrange[1]-temrange[0])/780.
        if tem<temrange[0]:   tem = temrange[0]
        elif tem>temrange[1]: tem = temrange[1]
        ind = int((tem - temrange[0])/scale)
        return self.__data[ind,:]

if __name__ == '__main__':
    import sys,os
    parpath = os.path.split(sys.argv[0])[0]
    tr = Tem2Rgb(parpath+'/tem_rgb.npy')
    print tr.getrgb(7000,[1000,8000])