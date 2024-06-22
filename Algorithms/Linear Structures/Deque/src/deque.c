#ifndef DEQUE_HEADER
#define DEQUE_HEADER
#include "deque.h"
#endif

deque* deque_create(){
    deque* ndq= (deque*) malloc(sizeof(deque));
    ndq->count= 0;
    ndq->start= NULL;
    ndq->end= NULL;
    return ndq;
}

dq_node* dq_node_create(void* p){
    dq_node* ndqn= (dq_node*) malloc(sizeof(dq_node));
    ndqn->payload= p;
    ndqn->next= NULL;
    ndqn->prev= NULL;
    return ndqn;
}

void* dq_node_get_payload(dq_node* dqn){
    return dqn->payload;
}

void deque_push(deque* dq, void* p){
    dq_node* e= dq_node_create(p);
    if(dq->start == NULL && dq->end == NULL){
        dq->start= e;
        dq->end= e;
    }
    if(dq->start != NULL && dq->end != NULL){
        e->prev= dq->end;
        dq->end->next=e;
        dq->end= e;
    }
    dq->count++;
}

dq_node* deque_pop(deque* dq){
    dq_node* e= dq->end;
    dq->end= e->prev;
    e->prev->next= NULL;
    e->prev= NULL;
    dq->count--;
    return e;
}

dq_node* deque_pull(deque* dq){
    dq_node* e= dq->start;
    dq->start= e->next;
    dq->start->prev= NULL;
    dq->count--;
    return e;
}

uint32_t deque_is_empty(deque* dq){
    return dq->count == 0 ? UINT32_MAX : 0;
}

void* deque_peek_start(deque* dq){
    return dq->start->payload;
}

void* deque_peek_end(deque* dq){
    return dq->end->payload;
}

int32_t deque_get_count(deque* dq){
    return dq->count;
}

void deque_clear(deque* dq){
    dq_node* p= dq->start;
    dq_node* pr= dq->start;
    while(p != NULL){
        pr= p->next;
        free(p);
        p= pr;
    }
    dq->start= NULL;
    dq->end= NULL;
    dq->count= 0;
}

void deque_free(deque* dq){
    dq_node* p= dq->start;
    dq_node* pr= dq->start;
    while(p != NULL){
        pr= p->next;
        free(p);
        p= pr;
    }
    free(dq);
}