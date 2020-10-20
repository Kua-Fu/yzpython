#include <stdio.h>

int main() {
    char name[100];
    printf("hello, world!\n");
    printf("What is your name?\n");
    scanf("%s",name);
    printf("Hello,%s,nice to meet you!\n",name);
}