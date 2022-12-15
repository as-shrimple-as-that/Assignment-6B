iterations = int(input('ey mate how many numbers do ya want?'))
Pi = 0
a = 1
b = 1
for i in range(iterations):
	if b == 1:
		Pi = Pi + (4/a)
	else:
		Pi = Pi - (4/a)
	print('Pi is currently equal to:        ' + str(Pi))
	a = a + 2
	b = b*-1
	print('The divisor is currently:  ' + str(a))
	continue