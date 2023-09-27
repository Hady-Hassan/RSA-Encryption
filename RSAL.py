import math
P  = int(input("enter a prime number P: "))
Q  = int(input("enter a prime number Q: "))
N  = P*Q
eN = (P-1)*(Q-1)
E  = int(input("enter e between 1 & euler: "))
M  = int(input("enter your message: "))

#encryption
C = pow(M, E)
C =int(math.fmod(C, N)) 
print("EnCrypted data = ", C)

#k define
def KDet(E, eN):
    for K in range(1, eN):
        D =int((1 + (K*eN))/E)
        if ((D*E)-(1+(K*eN)) == 0):
            return K
    return -1

#decryption
#Calculate K
K = KDet(E,eN)
print("the key = ",K)
D = int((1 + (K*eN))/E)
print("the D = ",D)

Fm1 = C**D
Fm = Fm1 % N
print("Original Message Sent = ", Fm)