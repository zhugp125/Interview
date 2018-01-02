#ifndef BINARYTREE_H
#define BINARYTREE_H

struct BinaryTree
{
    int value;
    struct BinaryTree* left;
    struct BinaryTree* right;
};
typedef struct BinaryTree BinaryTree;


#endif // BINARYTREE_H
