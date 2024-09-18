#include <stdio.h>
#include <unistd.h>//Para utilizar o sleep
#include <pthread.h>
#include <stdlib.h>
#include <sys/syscall.h>
#define NUM_THREADS 25

void *printHello(void *threadid){
    int tid = *(int*)threadid;
    printf("Olá! Sou a thread #%d(%d)!\nNo sistema sou <%ld>\nE meu PID no sistema sou %lu\n", tid, getpid(), pthread_self(), syscall(__NR_gettid));
    int teste = ((25 + 1) * (45 * 3)) / 3;
    printf("%d", teste);
    pthread_exit(NULL);
}

int main (int argc, char *argv[]){
    pthread_t threads[NUM_THREADS];
    int rc, t;
    for(t=0; t<NUM_THREADS; t++){
        printf("main: criando thread %d\n", t);
        rc = pthread_create(&threads[t], NULL, printHello, (void *)&t);
        if(rc){
            printf("Erro");
            exit(-1);
        }
    }
    for (t=0; t<NUM_THREADS; t++){
        pthread_join(threads[t], NULL);
    }
}