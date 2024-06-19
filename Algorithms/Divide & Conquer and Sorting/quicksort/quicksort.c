#include <stdint.h>

void quicksort(uint32_t arr[], int32_t st, int32_t en);
int32_t partition(uint32_t arr[], int32_t st, int32_t en);
void swap(uint32_t arr[], int32_t i, int32_t j);

void quicksort(uint32_t arr[], int32_t st, int32_t en){
    if((en - st) < 1)
        return;
    int32_t p= partition(arr, st, en);
    quicksort(arr, st, p-1);
    quicksort(arr, p+1, en);
}

int32_t partition(uint32_t arr[], int32_t st, int32_t en){
    int32_t i=st, j=st;
    for(;i<en;i++)
        if(arr[i] <= arr[en])
            swap(arr, i, j++);
    swap(arr, en, j);
    return j;
}

void swap(uint32_t arr[], int32_t i, int32_t j){
    if(i != j){
        uint32_t tmp= arr[i];
        arr[i]= arr[j];
        arr[j]= tmp;
    }
}