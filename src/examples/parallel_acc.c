#include <stdio.h>
#include <unistd.h>//Para utilizar o sleep
#include <pthread.h>
#include <stdlib.h>
#include <sys/syscall.h>
#define NUM_THREADS 25
int acc = 0;

void *printHello(void *threadid){
    int tid = *(int*)threadid;
    acc += tid;
    pthread_exit(NULL);
}

int main (int argc, char *argv[]){
    pthread_t threads[NUM_THREADS];
    int t;
    for(t=0; t<NUM_THREADS; t++){
        pthread_create(&threads[t], NULL, printHello, (void *)&t);
    }
    for (t=0; t<NUM_THREADS; t++){
        pthread_join(threads[t], NULL);
    }
    printf("%d", acc);
}