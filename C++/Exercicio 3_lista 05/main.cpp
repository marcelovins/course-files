#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main()
{
    char nome[50],sexo;
    int idade;
    printf("type your name:\n\n");
    gets(nome);
    printf("\ntype M for Male or F for Female:\n\n");
    scanf("%c",&sexo);
    printf("\ntype your age:\n\n");
    scanf("%d",&idade);

    if (sexo == 'f' || sexo == 'F' && idade<25)
    {
        printf("\n%s\n\nACEPTED\n\n",nome);
    }
        else
        {
            printf("\nNOT ACEPTED\n\n");
        };
    system("Pause");
    return 0;
}
