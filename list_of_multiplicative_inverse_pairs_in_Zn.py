def all_mi_pairs (n) :
#Generate all the multiplicative inverse pairs of n

	lans = list()

	for i in range(n+1) :
		for j in range(n+1) :
			if (i*j - 1) % n == 0 and [j,i] not in lans :
				lans.append([i,j])
	print("List of all pairs of multiplicative inverses: ")
	print (lans)
	print("Number of multiplicative inverse pairs: ", len(lans))

n=int(input("Enter a number: "))
all_mi_pairs(n)
