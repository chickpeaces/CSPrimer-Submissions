import time as t

TEST_LIMIT= 10000

def linear_fb_sum(x):
    output= 0
    for x in range(1,x+1):
            if x % 3 == 0:
                    output+= x
            if x%5 == 0 and x%3 != 0:
                    output+= x
    return output

def const_fb_sum(x): 
    return sum_m_n(x//3,3) + sum_m_n(x//5,5) - sum_m_n(x//15,15)

def sum_m_n(x, n):
    '''SUM of  1..k is (k*(k+1))/2'''
    return (n * (x * (x+1))) // 2

if __name__ == '__main__':
    linear_time= 0
    const_time= 0
    linear_sum= 0 
    const_sum= 0
    for x in range(1,TEST_LIMIT+1):
        #linear_fb_sum
        start= t.time()
        linear_sum= linear_fb_sum(x)
        end= t.time()
        linear_time+= (end-start)
        #const_fb_sum
        start= t.time()
        const_sum= const_fb_sum(x)
        end= t.time()
        const_time+= (end-start)
        assert linear_sum == const_sum, "failed at test case {}".format(x)

    print( "linear elapsed time: {:.5}s".format(linear_time))
    print( "const elapsed time: {:.5}s".format(const_time))