#include "hashmap.h"

Hashmap *Hashmap_new(void){
    Hashmap *nhmp= (Hashmap*) malloc(sizeof(Hashmap));
    nhmp->size= 0;
    nhmp->cap= STARTING_BUCKETS;
    nhmp->ld_fact= 0.0f;//does not use load factor
    nhmp->arr= (hmap_node**) calloc(nhmp->cap, sizeof(hmap_node*));
    for(int i=0;i<STARTING_BUCKETS;i++)
        nhmp->arr[i]=NULL;
    return nhmp;
}

int Hashmap_set(Hashmap *hmp, const char *key, void *val){
    int sl= hash_basic(key, hmp->cap);
    hmap_node *pptr, *ptr = hmp->arr[sl];

    if(ptr == NULL){
        hmp->arr[sl]= hmap_node_new(key, val);
        hmp->size++;
        return 1;
    }

    while(hmap_node_has_key(ptr)){
        if(strcmp(ptr->key,key) == 0){
            ptr->val= val;
            return 0;//node modified but not added
        }
        pptr= ptr;
        ptr= ptr->next;
    }

    pptr->next= hmap_node_new(key, val);
    hmp->size++;
    return 1;
}

void *Hashmap_get(Hashmap *hmp, const char *key){
    int sl= hash_basic(key, hmp->cap);
    hmap_node *ptr = hmp->arr[sl];

    while(hmap_node_has_key(ptr)){
        if(strcmp(ptr->key,key) == 0)
            return ptr->val;
        ptr= ptr->next;
    }

    return NULL;
}

void Hashmap_delete(Hashmap *hmp, const char *key){
    int sl= hash_basic(key, hmp->cap);
    hmap_node *pptr, *ptr = hmp->arr[sl];
    pptr= ptr;

    if(strcmp(hmp->arr[sl]->key,key) == 0){
        hmp->arr[sl]= ptr->next;
        hmap_node_delete(ptr);
        hmp->size--;
    }else{
        while(hmap_node_has_key(ptr)){
            if(strcmp(ptr->key,key) == 0){
                pptr->next= ptr->next;
                hmap_node_delete(ptr);
                hmp->size--;
                break;
            }
            pptr= ptr;
            ptr= ptr->next;
        }
    }
}

void Hashmap_free(Hashmap* hmp){
    hmap_node *ptr, *pptr;
    for(int i=0; i< hmp->cap;i++){
        pptr= ptr= hmp->arr[i];
        while(ptr != NULL){
            pptr= ptr;
            ptr=ptr->next;
            hmap_node_delete(pptr);
        }
    }
    free(hmp);
}

int hash_basic(const char* key, int mod){
    int h= 0;
    for(int i= 0;key[i] != '\0'; i++)
        h+= (int)key[i];
    return h% mod;
}