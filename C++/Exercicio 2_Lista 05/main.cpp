#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
    char nome[30],endereco[150],telefone[50];
    printf("digite seu nome:\n");
    gets(nome);
    printf("digite seu endereco:\n");
    gets(endereco);
    printf("digite seu telefone com ddd:\n");
    gets(telefone);
    printf("\n\nnome: %s\nendereço: %s\ntelefone: %s\n",nome,endereco,telefone);
    system("Pause");
    return 0;
}
