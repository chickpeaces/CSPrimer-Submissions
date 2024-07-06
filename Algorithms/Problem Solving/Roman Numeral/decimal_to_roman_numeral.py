def decimal_to_roman_numeral(n):
	l=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	a=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	s=''
	for i in range(13):
		while n >= a[i]:
			s+= l[i]
			n-= a[i]
	return s

if __name__ == '__main__':
	assert(decimal_to_roman_numeral(1949) == 'MCMXLIX')
	assert(decimal_to_roman_numeral(3724) == 'MMMDCCXXIV')