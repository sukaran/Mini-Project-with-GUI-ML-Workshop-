#include<iostream>
#include<stdlib.h>
using namespace std;

int main() {
    int i;
    FILE *fp;

    fp=fopen("bigfakefile.txt","w");

    for(i=0;i<(102.4*10.24);i++) {
        fseek(fp,(102.4*10.24), SEEK_CUR);
        fprintf(fp,"C");
    }

    fclose(fp);
    return 0;
}
