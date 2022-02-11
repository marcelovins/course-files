#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
    char nome[30];
    int B;
    printf("digite seu nome:\n");
    scanf("%s",&nome);
    printf("As quatro primeiras letras\n");

    for (B=0;B<=3;B++)

    printf(" %c\n\n\n",nome[B]);
    system("Pause");
    return 0;
}

