/*
通过预编译器提供了一些功能，

(1) 预编译器是编译过程中单独执行的第一个步骤

(2) 两个最常用的预编译器是 #include指令（用于在编译期间把指定文件的内容包含进当前文件中）, #define指令（用任意字符序列替换一个标记）
*/

#include <stdio.h>

/*
文件包含
文件包含指令（即#include)指令， 使得处理大量的#define指令以及声明更加方便
*/

/*
宏替换
宏定义形式为: #define 名字 替换文本

*/

/*
条件包含

使用条件语句对预处理本身进行控制，这种条件语句的值是在预处理执行的过程中进行计算，
这种方式为在编译过程中根据计算所得的条件的值选择性的包含不同代码提供了一种手段

*/

#define cat(x, y) x ## y

// x = char[10];

void main() {
    int x = cat(1, 2);
    char a[] = "a";
    char a3;
    cat(a, 3) = 13;
    printf("res is %d \n", x);
    printf("a3 is %d \n", a3);
}


