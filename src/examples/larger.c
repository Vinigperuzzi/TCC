#include<stdio.h>
#include<stdlib.h>

float add(float op1, float op2){
    return op1 + op2;
}

float sub(float op1, float op2){
    return op1 - op2;
}

float mult(float op1, float op2){
    return op1 * op2;
}

float divi(float op1, float op2){
    return op1 / op2;
}

int main(void){
    while (1)
    {
        int choice;
        float result, op1, op2;
        printf("Por favor, indique uma operação:\n");
        printf("[1]. Soma\n[2]. Subtração\n[3]. Multiplicação\n[4]. Divisão\n[5]. Sair\n");
        scanf("%d", &choice);
        printf("Informe os operandos: ");
        scanf("%f%f", &op1, &op2);

        switch (choice)
        {
        case 1:
            result = add(op1, op2);
            break;

        case 2:
            result = sub(op1, op2);
            break;

        case 3:
            result = mult(op1, op2);
            break;

        case 4:
            result = divi(op1, op2);
            break;

        case 5:
            exit(0);
            break;
        
        default:
            printf("Operação inválida");
            break;
        }
        printf("O resultado é %.2f\n", result);
    }
}