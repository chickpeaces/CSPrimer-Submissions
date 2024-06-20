import time as t

TEST_EXPONENT_COUNT= 16384

def slow_exp(n, e):
    out= 1
    for x in range(e):
        out*= n
    return out

def fast_exp(n, e):
    out= 1
    m= n
    f= e
    while(f>0):
        if f % 2 == 0:
            m*= m
            f//= 2
        elif f % 2 == 1:
            out*= m
            f-= 1
    return out

if __name__ == '__main__':
    start= t.time()
    for x in range(1,TEST_EXPONENT_COUNT+1):
        assert slow_exp(10, x) == 10 ** x
    end= t.time()
    print( "slow_exp() elapsed time: {:.5}s".format( end-start))

    start= t.time()
    for x in range(1,TEST_EXPONENT_COUNT+1):
        assert fast_exp(10, x) == 10 ** x
    end= t.time()
    print( "fast_exp() elapsed time: {:.5}s".format( end-start))