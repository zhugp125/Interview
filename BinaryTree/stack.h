#ifndef STACK_H
#define STACK_H

#include <stdlib.h>
#include <stdbool.h>

#define MaxSize 100

struct BinaryTree
{
    int value;
    struct BinaryTree* left;
    struct BinaryTree* right;
};
typedef struct BinaryTree BinaryTree;

struct stack
{
    BinaryTree* values[MaxSize];
    int index;
};
typedef struct stack stack;

void pushItem(stack* s, BinaryTree* value);

BinaryTree* popItem(stack* s);

stack* createStack();

void deleteStack(stack* s);

bool empty(stack* s);

#endif // STACK_H
