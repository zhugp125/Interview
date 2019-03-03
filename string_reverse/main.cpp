#include <iostream>
#include <string.h>

using namespace std;

/**
 * 字符串反序
 * 例如 This is a macbook  -> sihT si a koobcam
 * 时间复杂度 On
*/

bool reverse(const char* input, char* output)
{
    if (nullptr == input || nullptr == output)
    {
        return false;
    }

    char sep = ' ';
    size_t index = 0;
    size_t size = strlen(input);
    for (size_t i = 0; i < size; ++i)
    {
        // 遇到空格或者字符串末尾，才会进行下一步的反转字符串
        if (input[i] != sep && i != size - 1)
        {
            continue;
        }

        // 遇到空格，从空格前一个字符开始反向遍历
        // 到字符串末尾，从当前位置开始反向遍历
        // 反向遍历的终止是到字符串开始或者遇到空格，这个for循环的下表j的类型不能是size_t
        for (int j = (i == size - 1) ? i : i - 1; (j >= 0) && input[j] != sep; --j)
        {
            output[index++] = input[j];
        }

        // 不是字符串末尾时，要在输出字符串末尾添加空格
        if (i != size - 1)
        {
            output[index++] = sep;
        }
    }
    return true;
}

int main()
{
    const char* input = "This is a macbook";
    char output[18] = {0};
    reverse(input, output);
    cout << output << endl;

    cout << "Hello World!" << endl;
    return 0;
}
