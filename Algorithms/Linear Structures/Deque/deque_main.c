#include <stdio.h>
#include <assert.h>
#ifndef DEQUE_HEADER
#define DEQUE_HEADER
#include "deque.h"
#endif

#define TEST_ELEMENT_COUNT 1000000

int main(void){
    void* test_ptr= NULL;
    dq_node* test_node= NULL;
    deque* test_dq= deque_create();
    int32_t *arr= (int32_t*) calloc(TEST_ELEMENT_COUNT, 4);
    
    assert(deque_is_empty(test_dq) > 0);
    /* test pushing 100000 elements onto deque structure */
    for(int i=0;i<TEST_ELEMENT_COUNT;i++){
        arr[i]= i+1;
        deque_push(test_dq, &arr[i]);
        assert(deque_peek_end(test_dq) == &arr[i]);
    }
    assert(deque_is_empty(test_dq) == 0);
    assert(deque_get_count(test_dq) == TEST_ELEMENT_COUNT);

    /* test stack-based removal of 10000 elements off of deque structure */
    for(int i=TEST_ELEMENT_COUNT-1;i>(TEST_ELEMENT_COUNT-10001);i--){
        test_node= deque_pop(test_dq);
        assert(dq_node_get_payload(test_node) == &arr[i]);
    }
    assert(deque_get_count(test_dq) == TEST_ELEMENT_COUNT-10000);

    /* test queue-based removal of 10000 elements off of deque structure */
    for(int i=0;i<10000;i++){
        test_node= deque_pull(test_dq);
        assert(dq_node_get_payload(test_node) == &arr[i]);
    }
    assert(deque_get_count(test_dq) == TEST_ELEMENT_COUNT-20000);

    /* test clear of deque structure */
    deque_clear(test_dq);
    assert(deque_is_empty(test_dq) > 0);

    deque_free(test_dq);
    free(arr);
    printf("OK");
    return 0;
}