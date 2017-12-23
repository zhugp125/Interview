#ifndef STACK_H
#define STACK_H

#include <malloc.h>

#define MaxSize 100

struct stack
{
    int values[MaxSize];
    int index;
}stack;

void pushItem(stack* s, int value);

int popItem(stack* s);

stack* createStack();

void deleteStack(stack* s);

#endif // STACK_H
