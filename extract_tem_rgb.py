#coding:utf-8
import numpy as np
file = open('g:\\raw_tem2rgb.txt','r')
buf = file.read()
buf = buf.replace('deg','')
buflst = buf.split(' ')
while True:
    try:
        ind = buflst.index('')
        del buflst[ind] #删除非法字符
    except:
        break

lines = int(len(buflst)/13.)
buflst = buflst[:lines*13]

print lines

newlst = [0]*lines*3
indx = 0
ii = []
for i in range(0,lines*13,13):
    newlst[indx:indx+3] = buflst[i+9:i+12]
    k = buflst[i]
    ii.append(k)
    if len(ii)==2:
        if ii[0]==ii[1]:
            ii = []
        else:
            print ii[1]
            del ii[0]
    indx+=3

array1 = np.array(newlst,dtype=np.uint8)
str = array1.tostring()
file = open('g://tem_rgb.txt','w')
file.write(str)
array2 = array1.reshape((lines,3))
np.save('g:/tem_rgb.npy',array2)
print array1.shape
print array2.shape


