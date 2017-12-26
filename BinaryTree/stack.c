#include "stack.h"

void pushItem(stack* s, BinaryTree* value)
{
    if(s == NULL || s->index >= MaxSize)
        return ;

    s->values[s->index] = value;
    ++(s->index);
}

BinaryTree* popItem(stack* s)
{
    if(s == NULL || s->index <= 0)
        return NULL;

    --(s->index);
    return s->values[s->index];
}

stack* createStack()
{
    stack* s = (stack*)malloc(sizeof(stack));
    if(s)
    {
        s->index = 0;
    }
    return s;
}

void deleteStack(stack* s)
{
    if(s)
    {
        free(s);
        s = NULL;
    }
}

bool empty(stack *s)
{
    if(s == NULL || s->index <= 0)
        return false;
    return true;
}
