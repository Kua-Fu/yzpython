#include <stdio.h>

/*
#define 指令可以把符号名（或者称为符号常量）定义为一个特定的字符串
#define 名字 替换文本

(1) 在该定义之后，程序中出现的所有在#define中定义的名字都将用相应的替换文本替换；

(2) 名字和普通的变量名一样（都是用字母开始的字母和数字序列）

(3) 替换文本可以是任何的字符序列，而不仅限于数字

(4) 被替换的名字，不能是用引号引起来，也不可以是其他名字的一部分
*/

#define LOWER 0

#define UPPER 300

#define STEP 20

void main() {
    printf("lower vlaue is %d \n", LOWER);
    printf("upper vlaue is %d \n", UPPER);
    printf("step vlaue is %d \n", STEP);
}