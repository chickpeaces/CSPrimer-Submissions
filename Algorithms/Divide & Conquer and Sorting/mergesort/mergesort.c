#include <stdint.h>
#include <stdlib.h>

void mergesort(uint32_t arr[], int32_t len);
void merge(uint32_t arr[], uint32_t left[], uint32_t right[], int32_t llen, int32_t rlen);

void mergesort(uint32_t arr[], int32_t len){
    if(len < 2)
        return;
    uint32_t mid= (len/2);
    uint32_t *left= (uint32_t*) calloc(mid, 4);
    uint32_t *right= (uint32_t*) calloc(len - mid, 4);
    for(int i=0;i<mid;i++)
        left[i]= arr[i];
    for(int i=mid;i<len;i++)
        right[i-mid]= arr[i];
    mergesort(left, mid);
    mergesort(right, len - mid);
    merge(arr, left, right, mid, len - mid);
    free(left);
    free(right);
}

void merge(uint32_t arr[], uint32_t left[], uint32_t right[], int32_t llen, int32_t rlen){
    uint32_t i, j, k;
    i= j= k= 0;
    while(i< llen && j< rlen){
        if(left[i] <= right[j]){
            arr[k++]= left[i++];
        }
        else if(right[j] < left[i]){
            arr[k++]= right[j++];
        }
    }
    while(i< llen)
        arr[k++]= left[i++];
    while(j< rlen)
        arr[k++]= right[j++];
}