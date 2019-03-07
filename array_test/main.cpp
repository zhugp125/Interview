#include <iostream>

using namespace std;

/*!
 * \brief getDuplication 查找指定范围的输入的重复个数
 * \param input 输入数组，值范围 0 ~ n - 1
 * \param n  输入数组长度
 * \param output 输出
 * \return 返回重复个数，未找到返回0
 * 时间复杂度 O(n)
 * 空间复杂度 O(n)
 */
int getDuplication(int input[], int n, int output[])
{
    if (nullptr == input || nullptr == output || n <= 0)
    {
        return 0;
    }

    for (int i = 0; i < n; ++i)
    {
        if (input[i] < 0 || input[i] >= n)
            return 0;
    }

    int *temp = new int[n]{0};
    for (int i = 0; i < n; ++i)
    {
        ++temp[input[i]];
    }

    int count = 0;
    for (int i = 0; i < n; ++i)
    {
        if (temp[i] > 1)
            output[count++] = i;
    }
    delete []temp;

    return count;
}

int ceilRange(int input[], int n, int start, int end)
{
    if (nullptr == input || n <= 0)
    {
        return 0;
    }

    int count = 0;
    for (int i = 0; i < n; ++i)
    {
        if (input[i] <= end && input[i] >= start)
            ++count;
    }
    return count;
}

/*!
 * \brief getDuplication 查找指定范围的输入的重复个数
 * \param input 输入数组，值范围 1 ~ n - 1
 * \param n  输入数组长度
 * \return -1：未找到,否则找到
 * 时间复杂度 O(nlogn)
 * 空间复杂度 O(1)
 */
int getDuplication(int input[], int n)
{
    if (nullptr == input || n <= 0)
    {
        return -1;
    }

    for (int i = 0; i < n; ++i)
    {
        if (input[i] <= 0 || input[i] >= n)
            return -1;
    }

    int start = 1;
    int end = n - 1;
    while (start <= end) {
        int middle = ((end - start) >> 1) + start;
        int count = ceilRange(input, n, start, middle);
        if (start == end)
        {
            if (count > 1)
                return start;
            else
                break;
        }

        if (count > (middle - start + 1))
            end = middle;
        else
            start = middle + 1;
    }
    return -1;
}

/*!
 * \brief getDuplication 查找指定范围的输入的重复个数
 * \param input 输入数组，值范围 0 ~ n - 1
 * \param n  输入数组长度
 * \param duplication 重复数
 * \return true：找到，false：未找到
 * 时间复杂度 O(n)
 * 空间复杂度 O(1)
 */
bool getDuplication_move(int input[], int n, int *duplication)
{
    if (nullptr == input || nullptr == duplication || n <= 0)
    {
        return false;
    }

    for (int i = 0; i < n; ++i)
    {
        if (input[i] < 0 || input[i] >= n)
            return false;
    }

    for (int i = 0; i < n; ++i)
    {
        while (input[i] != i) {
            if (input[i] == input[input[i]])
            {
                *duplication = input[i];
                return true;
            }
            swap(input[i], input[input[i]]);
        }
    }
    return false;
}

bool findNumber(int *matrix, int columns, int rows, int number)
{
    bool bFind = false;
    if (nullptr == matrix || columns <= 0 || rows <= 0)
    {
        return bFind;
    }

    int column = columns - 1;
    int row = 0;
    while (row < rows && column >= 0) {
        if (matrix[row * columns + column] == number)
        {
            bFind = true;
            break;
        }
        else if (matrix[row * columns + column] > number)
            --column;
        else
            ++row;
    }
    return bFind;
}

int main()
{
    int input[] = {2, 3, 5, 4, 3, 2, 6, 7};
    int size = sizeof(input) / sizeof(input[0]);

    {
        int output[8] = {0};
        int count = getDuplication(input, size, output);
        for (int i = 0; i < count; ++i)
        {
            cout << output[i] << " ";
        }
        cout << endl;
    }

    {
        int ret = getDuplication(input, size);
        if (ret != -1)
        {
            cout << ret << endl;
        }
    }

    {
        int ret = 0;
        if (getDuplication_move(input, size, &ret))
        {
            cout << ret << endl;
        }
    }

    int matrix[][4] = {
        {1, 2, 8, 9},
        {2, 4, 9, 12},
        {4, 7, 10, 13},
        {6, 8, 11, 15}
    };

    int columns = sizeof(matrix[0]) / sizeof(matrix[0][0]);
    int rows = sizeof(matrix) / sizeof(matrix[0]);
    cout << boolalpha << findNumber((int*)matrix, columns, rows, 14) << noboolalpha << endl;

    cout << "Hello World!" << endl;
    return 0;
}
