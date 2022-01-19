#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main()
{
    char nome[50],sexo;
    int idade;
    printf("digite seu nome:\n\n");
    gets(nome);
    printf("\ndigite M para masculino ou F para feminino:\n\n");
    scanf("%c",&sexo);
    printf("\ndigite sua idade:\n\n");
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
