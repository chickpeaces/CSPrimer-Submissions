#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

int binary_search(int *a, int l, int x){
    int lo, hi, mid;
    lo= 0, hi= l-1, mid= (lo+((hi-lo) / 2));
    while(lo <= hi){
        if(a[mid]==x)
            return mid;
        if(a[mid]>x)
            hi= mid-1;
        if(a[mid]<x)
            lo= mid+1;
        mid= (lo+((hi-lo) / 2));
    }
    return -1;
}

int iterative_search(int *a, int l, int x){
    for(int i= 0; i< l; i++)
        if(a[i] == x)
            return i;
    return -1;
}

double time_elapsed(struct timespec begin, struct timespec end){
    return (end.tv_sec - begin.tv_sec) + (end.tv_nsec - begin.tv_nsec)*1e-9f;
}

#define TEST_ARRAY_MAX_LENGTH 1000

int main(void){
    struct timespec ist_begin, ist_end, bst_begin, bst_end, tt_begin, tt_end;
    double bst= 0.0, ist= 0.0;
    int len= 1, *a= NULL;
    FILE *ib_data= fopen("data.csv","w");
    fprintf(ib_data, "length,iterative,binary\n");
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &tt_begin);
    printf("\n");
    do{
        printf("\riteration %d", len);
        a= realloc(a, sizeof(int) * len);
        a[len-1]= len;
        /* iterative search */
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &ist_begin);
        assert(iterative_search(a, len, len+1) == -1);
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &ist_end);
        /* binary search */
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &bst_begin);
        assert(binary_search(a, len, len+1) == -1);
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &bst_end);
        bst= time_elapsed(bst_begin, bst_end);
        ist= time_elapsed(ist_begin, ist_end);
        fprintf(ib_data, "%d,%f,%f\n", len, ist, bst);
        len+= 1;
    }while(a != NULL && len <= TEST_ARRAY_MAX_LENGTH);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &tt_end);
    printf("\nProgram terminated in %f seconds CPU time\n", time_elapsed(tt_begin, tt_end));
    fclose(ib_data);
    return 0;
}