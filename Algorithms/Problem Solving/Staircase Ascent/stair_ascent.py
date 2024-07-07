import time as t
TEST_STAIR_COUNT= 50

def dyn_ascent(n): #dynamic programming approach
	a=[1,1,2]
	for x in range(3,n+1):
		a.append(a[x-1]+a[x-2]+a[x-3])
	return a[-1] if n > 1 else 1

def rec_ascent(n): #recursive approach
	if n <= 0:
		return 1 if not n else 0
	return rec_ascent(n-1)+rec_ascent(n-2)+rec_ascent(n-3)

if __name__ == '__main__':
	dyn_time= 0 
	rec_time= 0
	dyn_total_time= 0
	rec_total_time= 0
	for n in range(1, TEST_STAIR_COUNT+1):
		start= t.time()
		dyn_output= dyn_ascent(n)
		dyn_time= t.time()-start
		dyn_total_time+= dyn_time
		print("(n={0}) Dynamic Programming elapsed time: {1:.02f}s".format(n,dyn_time))
		start= t.time()
		rec_output= rec_ascent(n)
		rec_time= t.time()-start
		rec_total_time+= rec_time
		assert(dyn_output == rec_output)
		print("(n={0}) Recursive elapsed time: {1:.02f}s".format(n,rec_time))
	print("(total) Dynamic Programming elapsed time: {0:.02f}s".format(dyn_total_time))
	print("(total) Recursive elapsed time: {0:.02f}s".format(rec_total_time))