def sum_even(a,b):
	count = 0 #starts at zero
	for i in range (a,b,1): #for every number in range a to b, increment of 1
		if (i % 2.0 == 0): #check if number has a remainder of zer hwen divided by 2
			count += i
	return count
print(sum_even(0,101))
