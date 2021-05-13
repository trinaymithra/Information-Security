def inverse_of_n (num,n) :
#Multiplicative inverse of a number in Zn

    for i in range(n+1) :
        if i*num % n == 1 :
            return i


def crt(a,m) :
    M=1
    for ele in m :
        M=M*ele
    Mi=[]
    for ele in m :
        Mi.append(int(M/ele))
    Mi_inverse = []
    for i in range(len(Mi)) :
        Mi_inverse.append(inverse_of_n(Mi[i],m[i]))
    x=0
    for i in range(len(a)) :
        x=x+(a[i]*Mi[i]*Mi_inverse[i])
    return x%M

a=[int(i) for i in input("Enter all 'a's: ").split()]
m=[int(i) for i in input("Enter all 'm's: ").split()]
print(crt(a,m))

def rdec(a,b,key) :
    #refer chinese remainder theorem file to check how crt works
    p1=crt([a[0],b[0]],key)
    p2=crt([a[0],b[1]],key)
    p3=crt([a[1],b[0]],key)
    p4=crt([a[1],b[1]],key)
    
    ps=[]
    ps = [p1,p2,p3,p4]
    return ps
    
PT,p,q = [int(i) for i in input("Enter c,p,q values: ").split()]
c = (PT**2) % (p*q)
a = c**((p+1)/4)
a1 = a % p
a2 = -a % p

b = c**((q+1)/4)
b1 = b % q
b2 = -b % q

key = [p,q]
a_list = [a1,a2]
b_list = [b1,b2]

print("Possible plain texts are: {}".format(rdec(a_list, b_list, key)))
