class GoppaPoly:
    def __init__(self, field):
        self.t = field.t
        self.roots = [0]*self.t
        self.roots_index = []

    def chooseRoots(self, field, x = [1, 5, 8]):
        self.roots_index = x
        for i in range(self.t):
            self.roots[i] = field.elem[x[i]]

    def printGoppa(self):
        print(self.t)
        self.printRoots()

    def printRoots(self):
        print('Roots: ')
        for i in range(self.t):
            print(bin(self.roots[i]), end='\t')
        print('')

    def computePoly(self, field, a):
        res = 1
        for i in range(self.t):
            slag = field.sumElem(a, self.roots[i])
            res = field.mulElem(slag,res)
        #print('Poly(',bin(a),') =', bin(res))
        return res
