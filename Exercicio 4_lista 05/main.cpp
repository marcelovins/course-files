#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <conio.h>

using namespace std;

int main()
{
    string nome[50];
    int B;
    for(B=0;B<4;B++)
    {
        printf("\ndigite o nome:\n");
        scanf("%s", &nome[B]);
        printf("\n\nNomes: %s\n\n",nome[B]);
    }
    return 0;
}
