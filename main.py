import FieldClass

#x= [int(i) for i in input().split()]
x = [1, 0, 0, 1, 1]
print(x)

nf = FieldClass.FieldG(4, 3, x)
nf.printAboutField()
nf.createAllElements()
nf.printAllElem()
a = nf.elem[6]
b = nf.elem[9]
c = nf.elem[13]
d = nf.elem[3]
print('sum:',bin(nf.sumElem(a, b, c, d)))
print('mul:',bin(nf.mulElem(a, d, c)))
print('del:',bin(nf.delElem(a, d, c)))