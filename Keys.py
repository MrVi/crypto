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

    def printAll(self):
        print('Secret Key: \n', self.secretKey)
        print('Public Key: \n', numpy.matrix(self.publicKey))
        print('H mantrix: \n', numpy.matrix(self.Hmatrix))

    def randomListOfElem(self, goppa):
        random_list = [i for i in range(self.elem_num)]
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

    def gaussChange(self):
        max_str = getStringNumber(self.Hmatrix)
        print('max_str:', max_str)
        max_col = getColumnNumber(self.Hmatrix)
        print('max_col:', max_col)
        for k in range(max_str - 1):
            #bubble_max_row(self.Hmatrix, k)
            find_max_row(self.Hmatrix,k)
            for l in range(k + 1, max_str):
                if (self.Hmatrix[l][k] == 1):
                    for p in range(k, max_col):
                        self.Hmatrix[l][p] = (self.Hmatrix[l][p] + self.Hmatrix[k][p]) % 2


    def generateKeys(self, field, goppa):
        random_list = self.randomListOfElem(goppa)
        #random_list = [0, 10, 2, 9, 14, 7, 12, 3, 13, 4, 11, 6, 15]
        #print(random_list)
        self.createHmatrix(field, goppa, random_list)
        self.printAll()
        self.gaussChange()
        #make_generator_matrix(self.Hmatrix)
        print('H mantrix: \n', numpy.matrix(self.Hmatrix))
        # self.secretKey += random_list
        # print(self.secretKey)


