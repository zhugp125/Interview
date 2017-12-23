#include <stdio.h>
#include "stack.h"

struct BinaryTree
{
    int value;
    struct BinaryTree* left;
    struct BinaryTree* right;
};

typedef struct BinaryTree BinaryTree;

/**
 * @brief createNode  生成一个节点
 * @param value       当前节点的值
 * @return            返回生成的节点指针
 */
BinaryTree* createNode(int value)
{
    BinaryTree* tree = (BinaryTree*)malloc(sizeof(BinaryTree));
    if(tree)
    {
        tree->value = value;
        tree->left = NULL;
        tree->right = NULL;
    }
    return tree;
}

/**
 * @brief createBinaryTree  生成一个二叉树
 * @param value             根节点的值
 * @return                  返回二叉树的根节点
 */
BinaryTree* createBinaryTree(int value)
{
    return createNode(value);
}

/**
 * @brief addToLeftNode 添加值到二叉树的左节点
 * @param tree          插入的父节点
 * @param value         插入值
 * @return              插入的节点指针
 */
BinaryTree* addToLeftNode(BinaryTree* tree, int value)
{
    if(!tree)
        return NULL;

    BinaryTree* left = createNode(value);
    if(left == NULL)
        return NULL;

    tree->left = left;
    return left;
}

/**
 * @brief addToRightNode 添加值到二叉树的右节点
 * @param tree           插入的父节点
 * @param value          插入值
 * @return               插入的节点指针
 */
BinaryTree* addToRightNode(BinaryTree* tree, int value)
{
    if(!tree)
        return NULL;

    BinaryTree* right = createNode(value);
    if(right == NULL)
        return NULL;

    tree->right = right;
    return right;
}

/*!
 * \brief destory 销毁二叉树
 * \param tree    二叉树的根节点
 */
void destory(BinaryTree* tree)
{
    if(!tree)
        return;

    destory(tree->left);
    destory(tree->right);
    free(tree);
}

/**
 * @brief prevTraversal 前序遍历二叉树
 * @param tree          二叉树的根节点
 * 遍历思路：先遍历父节点，然后遍历左节点，最后遍历右节点
 */
void prevTraversal(BinaryTree* tree)
{
    if(!tree)
    {
        return ;
    }

    printf("value = %d\n", tree->value);
    prevTraversal(tree->left);
    prevTraversal(tree->right);
}

/**
 * @brief noPrevTraversal
 * @param tree
 */
void noPrevTraversal(BinaryTree* tree)
{
    if(!tree)
    {
        return ;
    }

    stack* st = createStack();
    if(st == NULL)
        return;
}

/**
 * @brief midTraversal  中序遍历
 * @param tree          二叉树的根节点
 * 遍历思路：先遍历左节点，然后遍历父节点，最后遍历右节点
 */
void midTraversal(BinaryTree* tree)
{
    if(!tree)
    {
        return ;
    }

    prevTraversal(tree->left);
    printf("value = %d\n", tree->value);
    prevTraversal(tree->right);
}

/**
 * @brief postTraversal 后序遍历
 * @param tree          二叉树的根节点
 * 遍历思路：先遍历左节点，然后遍历右节点，最后遍历父节点
 */
void postTraversal(BinaryTree* tree)
{
    if(!tree)
    {
        return ;
    }

    prevTraversal(tree->left);
    prevTraversal(tree->right);
    printf("value = %d\n", tree->value);
}

int main()
{
    BinaryTree* root = createBinaryTree(11);
    BinaryTree* left = addToLeftNode(root, 5);
    BinaryTree* right = addToRightNode(root, 10);

    BinaryTree* left_1 = addToLeftNode(left, 2);
    BinaryTree* left_2 = addToRightNode(left, 4);

    BinaryTree* right_1 = addToLeftNode(right, 7);
    BinaryTree* right_2 = addToRightNode(right, 9);

    addToLeftNode(left_1, 1);
    addToRightNode(left_2, 3);

    addToRightNode(right_1, 6);
    addToLeftNode(right_2, 8);

    //前序遍历
    printf("\nprev traversal :\n");
    prevTraversal(root);

    //中序遍历
    printf("\nmid traversal :\n");
    midTraversal(root);

    //后序遍历
    printf("\nmid traversal :\n");
    postTraversal(root);

    destory(root);

    printf("Hello World!\n");
    return 0;
}
