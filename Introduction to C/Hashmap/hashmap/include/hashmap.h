#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#define STARTING_BUCKETS 8
#define LOAD_FACTOR 0.70f
#define MAX_BUCKETS 1024
#define MAX_KEY_SIZE 247

typedef struct hmap_node{
    void *val;
    struct hmap_node *next;
    char key[MAX_KEY_SIZE];
} hmap_node;

typedef struct Hashmap{
    uint32_t size;
    uint32_t cap;
    float ld_fact;
    hmap_node** arr;
} Hashmap;

/* hmap_node function declarations*/
hmap_node *hmap_node_new(const char *k, void *v);
void hmap_node_delete(hmap_node *hn);
void hmap_node_set(hmap_node *hn, const char *k, void *v);
int hmap_node_has_key(hmap_node *hn);
int hmap_node_has_val(hmap_node *hn);
/*Hashmap function declarations*/
Hashmap *Hashmap_new(void);
int Hashmap_set(Hashmap *hmp, const char *key, void *val);
void *Hashmap_get(Hashmap *hmp, const char *key);
void Hashmap_delete(Hashmap *hmp, const char *key);
void Hashmap_free(Hashmap *hmp);
void Hashmap_resize(Hashmap *hmp);
int hash_basic(const char* k, int mod);