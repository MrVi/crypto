class FieldG:
    def __init__(self, mDeg = 4, tMist = 3, sec_from_user = [1, 0, 0, 1, 1]):
        self.m = mDeg
        self.t = tMist
        self.poly = polyCreate(sec_from_user)
        self.elem = []
        self.elem_num = 2 ** self.m

    def printAboutField(self):
        print('About field:')
        print( 'GF(2^m) = GF(',2 ** self.m,')')
        print('Find ', self.t, 'mistakes')
        printPoly(self.poly)

    def createAllElements(self):
        number_of_elem = self.elem_num
        self.elem = [0] * number_of_elem
        for i in range(number_of_elem):
            if i in range(self.m):
                self.elem[i] = 1 << i
            elif (i == (number_of_elem - 1)):
                self.elem[i] = 0
            else:
                 self.elem[i] = self.elem[i - 1] << 1
                 if (self.elem[i] > (number_of_elem - 1)):
                     self.elem[i] &= (number_of_elem - 1)
                     self.elem[i] ^= self.poly & (number_of_elem - 1)

    def printAllElem(self):
        print('Element of the GF(',2**self.m,'):')
        for i in range(self.elem_num):
            print(i,'\t', bin(self.elem[i]),'\t', self.elem[i])

    def sumElem(self,*a):
        sum = 0
        for i in range(len(a)):
           sum ^= a[i]
        return sum

    def mulElem(self,*a):
        mul = a[0]
        for i in range(1,len(a)):
            ind_res = (self.elem.index(mul) + self.elem.index(a[i])) \
                      % (self.elem_num - 1)
            mul = self.elem[ind_res]
        return mul

    def delElem(self, *a):
        delres = a[0]
        for i in range(1,len(a)):
            ind_res = (self.elem.index(delres) - self.elem.index(a[i])) \
                      % (self.elem_num - 1)
            delres = self.elem[ind_res]
        print(self.elem.index(delres))
        return delres


def polyCreate(x):
    poly = 0
    for i in range(len(x)):
        if x[i] == 1:
            poly += 1 << len(x) - 1 - i
    return poly

def printPoly(poly):
    print('Poly to create the field: ', poly, bin(poly))
