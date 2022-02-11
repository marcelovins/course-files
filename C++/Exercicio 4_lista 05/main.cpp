#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>

using namespace std;

int main()
{
    char nome[50];
    int B,tam;
    for(B=0;B<4;B++)
    {
        printf("\ndigite o nome:\n");
        gets(nome);
        tam=strlen(nome);
        printf("\n\nEsse nome tem %d letras\n\n",tam);
    }
    return 0;
}
