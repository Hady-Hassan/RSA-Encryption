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
def exteuc(eN,E):
    r = [eN , E]
    x = [0 , 1]
    q = [0 , 0]
    D = 0
    i = 2
    
    while True:
        q.append(int(r[i-2]/r[i-1]))
    
        r1 = (r[i-2]/r[i-1])-int(r[i-2]/r[i-1])
        
        r2 = r[i-1]
       
        r.append(round(r1 * r2))
        
        x.append(x[i-2]-(x[i-1]*q[i]))
       
        if(r[i]==1): 
            D = x[i]
            break
        i+=1
        
    if(D<0):
        D = D + eN
    return D

#decryption


D = exteuc(eN,E)
print("the D = ",D)

Fm1 = C**D
Fm = Fm1 % N
print("Original Message Sent = ", Fm)