/**
 * 字符串反序
 * 输入char* input，输出char* output
 * 例如 This is a macbook  -> sihT si a koobcam
 * 充分考虑各种情况
 * 时间复杂度 On
*/
#include <string.h>
void reverse(char *input, int &len, char *output, int &n)
{
    if(input == nullptr || output == nullptr || len <= 0)
        return ;

    for(int k = len - 1; k >= 0; --k)
    {
        output[n++] = input[k];
    }
    len = 0;
}

char* reverse(char* input, char *output)
{
    if(input == nullptr)
        return nullptr;

    int len = strlen(input);
    if(output != nullptr)
        delete output;

    output = new char[len + 1];
    char temp[48];
    int j = 0, n = 0;
    for(int i = 0; i < len; ++i)
    {
        if(input[i] != ' ')
        {
            temp[j++] = input[i];
        }
        else if(j != 0 || i == len - 1)
        {
            reverse(temp, j, output, n);
            output[n++] = ' ';
        }

        if(i == len - 1 && j != 0)
        {
            reverse(temp, j, output, n);
        }
    }

    return output;
}

struct Node
{
    int m_value;
    Node *m_next;

    Node(int i = 0) :m_value(i), m_next(nullptr) {}
};

//链表反转
Node * reverse(Node *head)
{
    Node *node = head;
    Node *prev = nullptr;

    while(node)
    {
        Node *temp = node->m_next;

        node->m_next = prev;
        prev = node;
        node = temp;
    }

    return prev;
}

算法——最短路径问题