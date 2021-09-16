def st(ch, step):
	k = ch
	for i in range(step - 1):
		ch = ch * k
	return(ch)


print(st(2, 5))
