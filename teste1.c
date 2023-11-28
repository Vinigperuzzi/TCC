#include<stdio.h>
#include<stdlib.h>

float calc(float v1, char op, float v2){
    switch (op)
    /*Um monte
    de comentário
    aqui
    só para ver qual que é*/
    {
    case '+':
        return v1 + v2;
        break;
    case '-':
        return v1 - v2;
        break;
    case '*':
        return v1 * v2;
        break;
    case '/':
        return v1 / v2;
        break;
    default:
    printf("\nOperador não reconhecido.\n\n");
        return -1;
        break;
    }
}


int main (void){
    int varTeste = 32;
    float v1, v2;
    char op;
    printf("Informe a operação a ser executada com espaços entre os valores:\n");
    scanf("%f", &v1);
    getchar();
    scanf("%c", &op);
    scanf("%f", &v2);
    float retorno = calc(v1, op, v2);
    printf("O resultado é %.2f.\n", retorno);
    if (varTeste == 32){
        varTeste = 0;
    }
}