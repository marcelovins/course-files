#include <stdio.h>
#include <stdlib.h>

int main()
{
    float a,b,c,d,e,v,saj,sap,spotencia,ct;
    int npessoas;
    char local,periodo;
    printf ("entre com o volume do ambiente em metros cubicos\n");
    scanf("%f",&v);
    printf("entre com a letra 'e' se o ambiente localiza-se entre andares,caso contrario, digite qualquer letra\n\n");
    scanf("%s",&local);
    if (local=='e' || local=='E')
    {
        a=v*16;
    }
    else
    {
        a=v*22.33;
    }
    printf("entre com a soma da area das janelas em metros quadrados. obs: considere as janelas da parede em que ha maior incidencia de luz solar\n\n");
    scanf("%f",&saj);
    printf("entre com a letra 'm' se as janelas ficam mais expostas sob a luz matutina e 't' caso sejam a tarde\n\n");
    scanf("%s",&periodo);
    if (periodo=='m' || periodo=='M')
    {
        b=saj*160;
    }
    else
    {
        b=saj*212;
    }
    printf("entre com o numero de pessoas que mais tempo permanecem no local\n");
    scanf("%d",&npessoas);
    c=npessoas*125;
    printf("entre com a soma da area das portas, em metros quadrados,que ficam abertas constantemente para ambientes nao condicionados\n");
    scanf("%f",&sap);
    d=sap*125;
    printf("entre com a soma da potencia em watts dos aparelhos eletricos que geram calor no ambiente, como: impressora, computadores, geladeiras, etc.\n\n");
    scanf("%f",&spotencia);
    e=spotencia*0.9;
    ct=a+b+c+d+e;
    printf("a potencia minima de seu ar condicionado, em kcal, devera ser de: %f",ct);

}
