#Generate all the multiplicative inverse pairs of a number 'n'
n=int(input("Enter a number: "))
ans = list()

for i in range(n+1) :
	for j in range(n+1) :
		if (i*j - 1) % n == 0 and [j,i] not in ans :
			ans.append([i,j])
      
print("List of all pairs of multiplicative inverses: ")
print (ans)
print("Number of miltiplicate inverses is", end = " ")
print(len(ans))
