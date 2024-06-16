#include "hashmap.h"

Hashmap *Hashmap_new(void){
    Hashmap *nhmp= (Hashmap*) malloc(sizeof(Hashmap));
    nhmp->size= 0;
    nhmp->cap= STARTING_BUCKETS;
    nhmp->ld_fact= LOAD_FACTOR;
    nhmp->arr= (hmap_node**) calloc(nhmp->cap, sizeof(hmap_node*));
    for(int i=0;i<STARTING_BUCKETS;i++)
        nhmp->arr[i]=NULL;
    return nhmp;
}

void Hashmap_resize(Hashmap *hmp){
    hmp->arr= (hmap_node**) realloc(hmp->arr, sizeof(hmap_node*) * (hmp->cap* 2));
    int dcap= hmp->cap*2;
    for(int i=hmp->cap; i<dcap;i++)
        hmp->arr[i]= NULL;
    hmp->cap= dcap;
}

int Hashmap_set(Hashmap *hmp, const char* key, void *val){
    int sl= hash_basic(key, hmp->cap);//starting hash location
    int nl= sl;                       //moving hash location, via open addressing algorithm

    do{
        if(hmp->arr[nl] == NULL){
            hmp->size++;
            if(((hmp->size / hmp->cap) >= hmp->ld_fact) && hmp->cap < MAX_BUCKETS)
                Hashmap_resize(hmp);//resize hashmap when at least 70% of buckets are full
            hmp->arr[nl]= hmap_node_new(key, val);
            return 1;
        }
        if(hmap_node_has_key(hmp->arr[nl]) && strcmp(hmp->arr[nl]->key, key) == 0){
            hmap_node_set(hmp->arr[nl], key, val);
            return 1;
        }
        nl= ++nl % hmp->cap;           //open addressing algorithm, +1 for each bucket collision
    }while(nl != sl);

    return 0;
}

void Hashmap_delete(Hashmap *hmp, const char* key){
    int sl= hash_basic( key, hmp->cap);
    int nl= sl;
    do{
        if(hmap_node_has_key(hmp->arr[nl]) && strcmp(hmp->arr[nl]->key, key) == 0){
            hmap_node_delete(hmp->arr[nl]);
            hmp->arr[nl]= NULL;
            hmp->size--;
            break;
        }
        nl= ++nl % hmp->cap;
    }while(nl != sl);
}

void *Hashmap_get(Hashmap *hmp, const char *key){
    int sl= hash_basic( key, hmp->cap);
    int nl= sl;
    do{
        if(hmap_node_has_key(hmp->arr[nl]) && strcmp(hmp->arr[nl]->key, key) == 0){
            return hmp->arr[nl]->val;
        }
        nl= ++nl % hmp->cap;
    }while(nl != sl);

    return NULL;
}

void Hashmap_free(Hashmap* hmp){
    for(int i=0; i< hmp->cap;i++)
        hmap_node_delete(hmp->arr[i]);
    free(hmp);
}

int hash_basic(const char* key, int mod){
    int h= 0;
    for(int i= 0;key[i] != '\0'; i++)
        h+= (int)key[i];
    return h% mod;
}