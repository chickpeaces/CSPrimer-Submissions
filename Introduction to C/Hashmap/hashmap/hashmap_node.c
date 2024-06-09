#include "hashmap.h"

hmap_node *hmap_node_new(const char* k, void* v){
    hmap_node *nhmpn= (hmap_node*) malloc(sizeof(hmap_node));
    nhmpn->val= v;
    strcpy(nhmpn->key, k);
    return nhmpn;
}

void hmap_node_delete(hmap_node* hn){
    free(hn);
}

void hmap_node_set(hmap_node* hn, const char* k, void* v){
    strcpy(hn->key, k);
    hn->val= v;
}

int hmap_node_has_value(hmap_node* hn){
    return (hn != NULL && hn->val != NULL) ? 1 : 0;
}

int hmap_node_has_key(hmap_node* hn){
    return (hn != NULL && hn->key != NULL) ? 1 : 0;
}