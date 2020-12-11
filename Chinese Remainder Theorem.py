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
