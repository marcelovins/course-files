#include <stdlib.h>
#include <stdio.h>
#include <math.h>

//Fun��o com passagem por referencia
void divide(int dividendo, int divisor, int &resto, int &quociente){
    quociente = floor(dividendo/divisor);

    //floor arredonda para baixo
    //ceil arredonda para cima
    //round arredonda para o mais pr�xmo

    resto = dividendo % divisor;
}


//Fun��o normal
int soma(int valor1){
    return ++valor1;  //valor1 = valor1 + 1;

    //valor1++;
    //return valor1;
}


int main(){
    /*
    int valor2;

    valor2=5;

    valor2=soma(valor2);

    printf("%d",valor2);
    */
    int valor1 = 10, valor2 = 3, r, q;
    divide(valor1,valor2,r,q);

    printf("Quociente: %d\nResto: %d\n\n",q,r);

    system("pause");
    return 0;
}
