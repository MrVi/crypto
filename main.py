import FieldClass
import GoppaClass
import Keys
from datetime import datetime

def newCryptosystem(m, t, n, field_polynom, goppa_roots, e):
    key_generation_time = 0
    encryption_time = 0
    decryption_time = 0
    """Field Creation"""
    nf = FieldClass.FieldG(m, t, field_polynom)
    nf.printAboutField()
    nf.createAllElements()
    nf.printAllElem()
    """Goppa polynom creation"""
    gm = GoppaClass.GoppaPoly(nf)
    gm.chooseRoots(nf, goppa_roots)
    #gm.printGoppa()
    """key generation """
    start_t = datetime.now()
    key = Keys.Key(nf, n)
    key.generateKeys(nf, gm)
    finish_t = datetime.now()
    key.printAll()
    key_generation_time = finish_t - start_t
    """encryption"""

    """decryption"""

    print('Work time for keys generation: ', key_generation_time)
    print('Work time for encryption: ', encryption_time)
    print('Work time for decryption: ', decryption_time)

#x= [int(i) for i in input().split()]
x = [1, 0, 0, 1, 0, 1]  # x^5+x^2+1
print(x)
m = 5
t = 3
n = 25
roots = [1, 5, 8]
e = [0]*n
newCryptosystem(m, t, n, x, roots, e)

"""
for GF(2^5)
Random List: 
 [29, 2, 14, 12, 15, 13, 27, 4, 9, 30, 6, 22, 10, 21, 0, 11, 20, 7, 24, 19, 26, 17, 23, 25, 16]
Work time for keys generation:  0:00:00.006004
x = [1, 0, 0, 1, 0, 1] # x^5+x^2+1
m = 5
t = 3
n = 25
roots = [1, 5, 8]
"""

"""
for GF(2^4)
x = [1, 0, 0, 1, 1]  #x^4+x+1
m = 4
t = 2
n = 12
roots = [1, 5]
"""

"""for GF(2^11)
x = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] #x^11+x^2+1
m = 11
t = 30
n = 1024
roots = [1, 3, 5, 8, 10, 23, 2, 100, 36, 34, 40, 50, 55, 37, 26, 27, 11, 13, 19, 41,
# 43, 53, 54, 76, 81, 85, 70, 71, 91, 99]
"""

"""
for GF(2^12)
Random List: 
x = ??
m = 12
t = 40
n = 2000
roots = ??
"""



"""
GF(2^2) x^2+x+1
GF(2^3) x^3+x+1
GF(2^4) x^4+x+1
GF(2^5) x^5+x^2+1   0:00:00.041529  
GF(2^6) x^6+x+1
GF(2^7) x^7+x^3+1
GF(2^8) x^8+x^4+x^3+x^2+1
GF(2^9) x^9+x^4+1
GF(2^10) x^10+x^3+1
GF(2^11) x^11+x^2+1   0:00:26.968836
GF(2^12) x^12+x^6+x^4+x+1
GF(2^13) x^13+x^4+x^3+x+1
GF(2^14) x^14+x^10+x^6+x+1
GF(2^15) x^15+x+1
GF(2^16) x^16+x^12+x^3+x+1
GF(2^17) x^17+x^3+1
GF(2^18) x^18+x^7+1
GF(2^19) x^19+x^5+x^2+x+1
GF(2^20) x^20+x^3+1
GF(2^21) x^21+x^2+1
GF(2^22) x^22+x+1
GF(2^23) x^23+x^5+1
GF(2^24) x^24+x^7+x^2+x+1
GF(2^25) x^25+x^3+1
GF(2^26) x^26+x^6+x^2+x+1
GF(2^27) x^27+x^5+x^2+x+1
GF(2^28) x^28+x^3+1
GF(2^29) x^29+x^2+1
GF(2^30) x^30+x^23+x^2+x+1
GF(2^31) x^31+x^3+1
GF(2^32) x^32+x^22+x^2+x+1
GF(2^36) x^36+x^11+1
GF(2^40) x^40+x^9+x^3+x+1
GF(2^48) x^48+x^28+x^3+x+1
GF(2^56) x^56+x^42+x^2+x+1
GF(2^64) x^64+x^46+x^4+x+1
GF(2^72) x^72+x^62+x^3+x^2+1
GF(2^80) x^80+x^54+x^2+x+1
GF(2^96) x^96+x^31+x^4+x+1
GF(2^128) x^128+x^7+x^2+x+1
GF(2^160) x^160+x^19+x^4+x+1
GF(2^192) x^192+x^107+x^4+x+1
GF(2^256) x^256+x^16+x^3+x+1
"""