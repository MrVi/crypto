import FieldClass
import GoppaClass
import Keys
from datetime import datetime

#x= [int(i) for i in input().split()]


x = [1, 0, 0, 1, 1]
print(x)
nf = FieldClass.FieldG(4, 3, x)
nf.printAboutField()
nf.createAllElements()
nf.printAllElem()
a = nf.elem[6]
b = nf.elem[0]
c = nf.elem[13]
d = nf.elem[15]
print('sum:',bin(nf.sumElem(a, b, c, d)))
print('mul:',bin(nf.mulElem(a, d)))
print('mul:',bin(nf.mulElem(a, b)))
print('mul:',bin(nf.mulElem(a, b, c)))
print('del:',bin(nf.delElem(a, d, c)))
gm = GoppaClass.GoppaPoly(nf)
gm.chooseRoots(nf)
gm.printGoppa()
gm.computePoly(nf,a)
gm.computePoly(nf,b)
k = gm.computePoly(nf,c)
gm.computePoly(nf,d)
print (nf.elemToList(k))

#key generation
start_t = datetime.now()

key = Keys.Key(nf,13)
key.printAll()
key.generateKeys(nf,gm)

finish_t = datetime.now()
print('Work time for keys generation: ', finish_t - start_t)

#coding

#decoding



# #SECOND
# print('SECOND')
#
# #x = [1, 0, 0, 1, 0, 1] #x^5+x^2+1
# x = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]#x^11+x^2+1
# print(x)
# nf = FieldClass.FieldG(11, 30, x)
# nf.printAboutField()
# nf.createAllElements()
# #nf.printAllElem()
#
# gm = GoppaClass.GoppaPoly(nf)
# t = [1, 3, 5, 8, 10, 23, 2, 100, 36, 34, 40, 50, 55, 37, 26, 27, 11, 13, 19, 41,
#      43, 53, 54, 76, 81, 85, 70, 71, 91, 99]
# gm.chooseRoots(nf, t)
# gm.printGoppa()
#
# #key generation
# start_t = datetime.now()
#
# key = Keys.Key(nf, 1024)
# key.printAll()
# key.generateKeys(nf,gm)
#
# finish_t = datetime.now()
# print('Work time for keys generation: ', finish_t - start_t)