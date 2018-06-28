#include<stdio.h>
#include<stdlib.h>

int main() {
    int i;
    FILE *fp;

    fp=fopen("bigfakefile1.txt","w");

    for(i=0;i<(10.24*102.4);i++) {
        fseek(fp,(10.24*102.4), SEEK_CUR);
        fprintf(fp,"C");
    }

    fclose(fp);
    return 0;
}
