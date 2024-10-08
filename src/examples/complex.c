#include <stdio.h>
#include <unistd.h>//Para utilizar o sleep
#include <pthread.h>
#include <stdlib.h>
#include <sys/syscall.h>
#define NUM_THREADS 26

int acc = 0;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *printHello(void *threadid){
    int tid = *(int*)threadid;
    //printf("Olá! Sou a thread #%d(%d)!\nNo sistema sou <%ld>\nE meu PID no sistema sou %lu\n", tid, getpid(), pthread_self(), syscall(__NR_gettid));
    printf("Fui criada com %d\n", tid);
    int local = acc;
    local += tid;
    acc = local;
    pthread_mutex_unlock(&mutex);
    pthread_exit(NULL);
}

int step(int t){
    pthread_mutex_lock(&mutex);
    pthread_mutex_lock(&mutex);
    t++;
    return t;
}

int main (int argc, char *argv[]){
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&mutex,NULL);
    int rc, t;
    for(t=0; t<NUM_THREADS; t = step(t)){
        int j = t + 1;
        printf("main: criando thread %d\n", j);
        rc = pthread_create(&threads[t], NULL, printHello, (void *)&j);
        pthread_mutex_unlock(&mutex);
        if(rc){
            printf("Erro");
            exit(-1);
        }
    }
    for (t=0; t<NUM_THREADS; t++){
        pthread_join(threads[t], NULL);
    }
    printf("\n\n%d\n\n", acc);
    pthread_mutex_destroy(&mutex);
}