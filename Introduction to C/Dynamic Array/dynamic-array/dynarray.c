#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define STARTING_CAPACITY 8

enum type{
  ch= 0,  //char 
  in,     //integer
  si,     //short
  li,     //long 
  ll,     //long long
  fl,     //float
  db      //double
};

typedef struct DA {
  short length;    //current number of items in DA
  short capacity;  //maximum number of items in DA
  void** array;    //memory holding references to items in DA
  char* type_array;
} DA;


DA* DA_new (void) {
  DA* da= malloc( sizeof( DA));
  da->length= 0;
  da->capacity= STARTING_CAPACITY;
  da->array= calloc( STARTING_CAPACITY, sizeof(void*));

  return da;
}

int DA_size(DA *da) {
  return da->length;
}

void DA_push (DA* da, void* x) {
  if( da->length >= da->capacity){
    da->array= realloc(da->array, (da->capacity*= 2) * sizeof(void*));
  }
  da->array[da->length++]= x;
}

void* DA_pop(DA *da) {
  if(da->length)
    return da->array[--da->length];

  return NULL;
}

void DA_set(DA *da, void *x, int i) {
  if( da->length && i < da->length)
    da->array[i]= x;
}

void* DA_get(DA *da, int i) {
  if(da->length && i < da->length)
    return da->array[i];

  return NULL;
}


void DA_free(DA *da) {
  for(int i= 0; i< da->length; i++)
    free(da->array[i]);
  free(da->array);
}

int main() {
    DA* da = DA_new();

    assert(DA_size(da) == 0);

    // basic push and pop test
    int x = 5;
    float y = 12.4;
    DA_push(da, &x);
    DA_push(da, &y);
    assert(DA_size(da) == 2);

    assert(DA_pop(da) == &y);
    assert(DA_size(da) == 1);

    assert(DA_pop(da) == &x);
    assert(DA_size(da) == 0);
    assert(DA_pop(da) == NULL);

    // basic set/get test
    DA_push(da, &x);
    DA_set(da, &y, 0);
    assert(DA_get(da, 0) == &y);
    DA_pop(da);
    assert(DA_size(da) == 0);

    // expansion test
    DA *da2 = DA_new(); // use another DA to show it doesn't get overriden
    DA_push(da2, &x);
    int i, n = 100 * STARTING_CAPACITY, arr[n];
    for (i = 0; i < n; i++) {
      arr[i] = i;
      DA_push(da, &arr[i]);
    }
    assert(DA_size(da) == n);
    for (i = 0; i < n; i++) {
      assert(DA_get(da, i) == &arr[i]);
    }
    for (; n; n--)
      DA_pop(da);
    assert(DA_size(da) == 0);
    assert(DA_pop(da2) == &x); // this will fail if da doesn't expand

    DA_free(da);
    DA_free(da2);
    printf("OK\n");
}
