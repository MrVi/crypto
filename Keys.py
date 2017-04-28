import numpy
import random
from MatrixOperations import *

class Key:
    def __init__(self, field, n):
        m = field.m
        t = field.t
        self.elem_num = 2 ** m
        self.n = n
        self.secretKey = []#[0] * (n + t)
        self.publicKey = [[0]*(n - m*t) for i in range(m*t)]
        self.Hmatrix = [[0]*(n) for i in range(t*m)]
        self.random_list = []

    def printAll(self):
        print('Secret Key: \n', self.secretKey)
        print('Public Key: \n', numpy.matrix(self.publicKey))
        print('H mantrix: \n', numpy.matrix(self.Hmatrix))
        print('Random List: \n', self.random_list)

    def randomListOfElem(self, goppa):
        random_list = [i for i in range(self.elem_num-1)]
        #print('rand', random_list)
        for i in range(goppa.t):
            random_list.remove(goppa.roots_index[i])
        random_list = random.sample(random_list, self.n)
        return random_list

    def createHmatrix(self, field, goppa, random_list):
        for j in range(len(random_list)):
            divident = field.elem[0]
            goppa_res = goppa.computePoly(field, field.elem[random_list[j]])
            #print('\nj:',j,'in_rand',random_list[j], 'goppa_res_ind', field.elem.index(goppa_res), 'a:', divident, 'end')
            for i in range(len(goppa.roots)):
                if i != 0 :
                    divident = field.mulElem(divident, field.elem[random_list[j]])
                #print('ji:', j, i, 'a_ind', field.elem.index(divident))
                res_of_divide = field.delElem(divident, goppa_res)
                #print('ji:', j, i,'res_after_del_ind', field.elem.index(res_of_divide))
                res_of_divide = field.elemToList(res_of_divide)
                for k in range(field.m):
                    self.Hmatrix[i*field.m + k][j] = res_of_divide[k]
        #print('H mantrix: \n', numpy.matrix(self.Hmatrix))

    def createSecretKey(self, field, goppa, random_list):
        for i in range(len(random_list)):
            self.secretKey.append(field.elem[random_list[i]])
        self.secretKey += goppa.roots

    def createPublicKey(self, H):
        max_str = getStringNumber(H)
        max_col = getColumnNumber(H)
        for i in range(max_str):
            for j in range (max_col - max_str):
                self.publicKey[i][j] = H[i][max_str + j]

    def generateKeys(self, field, goppa):
        self.random_list = self.randomListOfElem(goppa)
        """temp random_key """
        self.random_list = [29, 2, 14, 12, 15, 13, 27, 4, 9, 30, 6, 22, 10, 21, 0, 11, 20, 7, 24, 19, 26, 17, 23, 25, 16]
        self.createHmatrix(field, goppa, self.random_list)
        #self.printAll()
        k = 0
        gaussChange(self.Hmatrix)
        while (is_singular(self.Hmatrix)):
            self.random_list = self.randomListOfElem(goppa)
            #print(self.random_list)
            self.createHmatrix(field, goppa, self.random_list)
            gaussChange(self.Hmatrix)
            k += 1

        print('K', k)
        self.createSecretKey(field, goppa, self.random_list)
        self.createPublicKey(self.Hmatrix)
        #self.printAll()



