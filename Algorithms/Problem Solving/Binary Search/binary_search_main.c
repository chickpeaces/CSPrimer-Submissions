#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>

#define TEST_ARRAY_LENGTH 100000

int64_t binary_search_iterative(uint32_t a[], uint32_t l, int32_t x){
    uint32_t hi, lo, mid;
    hi= l-1, lo= 0, mid= (lo+((hi-lo) / 2));
    while(lo <= hi){
        if(a[mid] == x)
            return mid;
        if(a[mid] < x)
            lo= mid+1;
        if(a[mid] > x)
            hi= mid-1;
        mid= (lo+((hi-lo) / 2));
    }

    return -1;
}

int64_t binary_search_recursive(uint32_t a[], uint32_t hi, uint32_t lo, int32_t x){

    if(hi < lo || lo > hi)
        return -1;

    int32_t mid= (lo+((hi-lo) / 2));
    if(a[mid] > x)
        return binary_search_recursive(a, mid-1, lo, x);
    if(a[mid] < x)
        return binary_search_recursive(a, hi, mid+1, x);

    return mid;
}

int main(void){
    uint32_t test_case[TEST_ARRAY_LENGTH];
    for(uint32_t i=1; i<=TEST_ARRAY_LENGTH;i++)
        test_case[i-1]=i;
    int64_t idx= -1;
    for(uint32_t i=1; i<=TEST_ARRAY_LENGTH;i++){
        assert(idx=binary_search_iterative(test_case, TEST_ARRAY_LENGTH, i) == (i-1));
        assert(idx=binary_search_recursive(test_case, TEST_ARRAY_LENGTH-1, 0, i) == (i-1));
    }
    assert(idx=binary_search_iterative(test_case, TEST_ARRAY_LENGTH, TEST_ARRAY_LENGTH+1) < 0);
    assert(idx=binary_search_recursive(test_case, TEST_ARRAY_LENGTH-1, 0, TEST_ARRAY_LENGTH+1) < 0);
    assert(idx=binary_search_iterative(test_case, TEST_ARRAY_LENGTH, -1234) < 0);
    assert(idx=binary_search_recursive(test_case, TEST_ARRAY_LENGTH-1, 0, -1234) < 0);

    printf("OK");
    return 0;
}