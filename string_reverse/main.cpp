#include <iostream>
#include <string.h>

using namespace std;

/**
 * 字符串反序
 * 例如 This is a macbook  -> sihT si a koobcam
 * 时间复杂度 O(n)
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

class String
{
public:
    String(char* str = nullptr)
    {
        if (nullptr == str)
        {
            m_data = new char[1];
            m_data[0] = '\0';
        }
        else
        {
            int len = strlen(str);
            m_data = new char[len + 1];
            strcpy(m_data, str);
        }
    }

    String(const String& str)
    {
        int len = strlen(str.m_data);
        m_data = new char[len + 1];
        strcpy(m_data, str.m_data);
    }

    friend bool operator ==(const String& lhs, const String& rhs)
    {
        return !strcmp(lhs.m_data, rhs.m_data);
    }

    friend bool operator !=(const String& lhs, const String& rhs)
    {
        return !(lhs == rhs);
    }

    // 异常安全
    String& operator =(const String& str)
    {
        if (*this != str)
        {
            String strTemp(str);
            std::swap(strTemp.m_data, m_data);
        }
        return *this;
    }

    ~String()
    {
        delete[] m_data;
    }

    size_t size() const
    {
        return strlen(m_data);
    }

    char* c_str() const
    {
        return m_data;
    }

private:
    char* m_data;
};

/*
 * string to int
 * 考虑输入为空，输入负号，小数点前输入除负号以外的非数字字符
 * 考虑int越界的问题
 * 时间复杂度 O(n)
*/
int stringToInt(const char* s, bool *ok = nullptr)
{
    (ok != nullptr) ? (*ok = false) : 0;

    if (nullptr == s)
    {
        return 0;
    }

    int symbol = 1;
    if (*s == '-')
    {
        symbol = -1;
        ++s;
    }

    int nRet = 0;
    int nTemp = 0;
    do
    {
        if (*s == '.')
        {
            break;
        }
        else if (*s < '0' || *s > '9')
        {
            return 0;
        }

        nTemp = nRet;
        nRet *= 10;
        nRet += (*s - '0');
        if (nTemp > nRet)
        {
            return 0;
        }

        ++s;
    }while (*s);

    (ok != nullptr) ? (*ok = true) : 0;
    return nRet * symbol;
}

int main()
{
    const char* input = "This is a macbook";
    char output[18] = {0};
    reverse(input, output);
    cout << output << endl;

    cout << boolalpha;
    bool ok;
    int ret = stringToInt("", &ok);
    cout << ok << " " << ret << endl;

    ret = stringToInt("1234", &ok);
    cout << ok << " " << ret << endl;

    ret = stringToInt("-12.34", &ok);
    cout << ok << " " << ret << endl;

    ret = stringToInt("12a34", &ok);
    cout << ok << " " << ret << endl;

    cout << noboolalpha;

    cout << "Hello World!" << endl;
    return 0;
}
