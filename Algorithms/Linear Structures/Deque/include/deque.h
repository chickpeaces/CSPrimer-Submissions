#include <stdint.h>
#include <stdlib.h>

typedef struct dq_node{
    void* payload;
    struct dq_node* next;
    struct dq_node* prev;
}dq_node;

dq_node* dq_node_create(void* p);
void* dq_node_get_payload(dq_node* dqn);

typedef struct deque{
    int32_t count;
    dq_node* start;
    dq_node* end;
}deque;

deque* deque_create();
uint32_t deque_is_empty(deque* dq);
void deque_push(deque* dq, void* p);//Push to end of list
dq_node* deque_pop(deque* dq);      //Stack-based remove
dq_node* deque_pull(deque* dq);     //Queue-based remove
void* deque_peek_start(deque* dq);
void* deque_peek_end(deque* dq);
int32_t deque_get_count(deque* dq);
void deque_clear(deque* dq);
void deque_free(deque* dq);
