#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node* next;
}Node;

int main(){
    
    Node* newNode = (Node*)malloc(sizeof(Node));

    if(newNode == NULL){
        printf("Erro de memoria");
        return 1;
    }

    newNode->data = 10;
    newNode->next  = NULL;
    
    printf("Dado: %d\n", newNode->data);
    printf("Endereco do próximo: %p\n", (void*)newNode->next);
    

    free(newNode);

    return 0;
}