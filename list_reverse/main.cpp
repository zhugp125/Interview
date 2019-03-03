#include <iostream>

using namespace std;

typedef struct Node
{
    Node(int value = 0)
        : m_value(value)
        , m_next(nullptr)
    {}

    int m_value;
    struct Node* m_next;
}Node;

Node* reverse(Node* pHead)
{
    if (nullptr == pHead)
    {
        return nullptr;
    }

    Node* pNode = pHead;
    Node* pPrev = nullptr;

    while (pNode)
    {
        Node* pNext = pNode->m_next;

        pNode->m_next = pPrev;
        pPrev = pNode;
        pNode = pNext;
    }
    return pPrev;
}

void display(Node* pHead)
{
    if (nullptr == pHead)
    {
        return;
    }

    Node* pNode = pHead;
    while (pNode)
    {
        cout << pNode->m_value << " ";
        pNode = pNode->m_next;
    }
    cout << endl;
}

void destory(Node* pHead)
{
    if (nullptr == pHead)
    {
        return;
    }

    Node* pNode = pHead;
    while (pNode)
    {
        Node* pNext = pNode->m_next;

        delete pNode;
        pNode = pNext;
    }
    pHead = nullptr;
}

Node* create(int value)
{
    Node* pHead = new Node(value);
    return pHead;
}

void push_back(Node* pHead, Node* pNode)
{
    if (nullptr == pHead || nullptr == pNode)
    {
        return;
    }

    Node* pTemp = pHead;
    while (pTemp->m_next)
    {
        pTemp = pTemp->m_next;
    }
    pTemp->m_next = pNode;
}

Node* front_back(Node* pHead, Node* pNode)
{
    if (nullptr == pHead || nullptr == pNode)
    {
        return nullptr;
    }

    pNode->m_next = pHead;
    return pNode;
}

int length(Node* pHead)
{
    if (nullptr == pHead)
    {
        return -1;
    }

    Node* pNode = pHead;
    int len = 0;
    while (pNode)
    {
        ++len;
        pNode = pNode->m_next;
    }
    return len;
}

Node* find(Node* pHead, int value)
{
    if (nullptr == pHead)
    {
        return nullptr;
    }

    Node* pNode = pHead;
    while (pNode && pNode->m_value != value)
    {
        pNode = pNode->m_next;
    }
    return pNode;
}

int main()
{
    Node* pHead = create(1);
    push_back(pHead, new Node(2));
    push_back(pHead, new Node(3));
    push_back(pHead, new Node(4));
    pHead = front_back(pHead, new Node(0));
    pHead = front_back(pHead, new Node(-1));

    cout << "length: " << length(pHead) << endl;

    Node* pNode = find(pHead, 5);
    if (pNode != nullptr)
    {
        cout << pNode->m_value << endl;
    }

    display(pHead);

    pHead = reverse(pHead);
    display(pHead);

    destory(pHead);

    cout << "Hello World!" << endl;
    return 0;
}
