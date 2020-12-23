def rdec(a,b,key) :
    #refer chinese remainder theorem file to check how crt works
    p1=crt([a[0],b[0]],key)
    p2=crt([a[0],b[1]],key)
    p3=crt([a[1],b[0]],key)
    p4=crt([a[1],b[1]],key)
    
    ps=[]
    ps = [p1,p2,p3,p4]
    return ps
    
c,p,q = [int(i) for i in input("Enter c,p,q values: ").split()]
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
