#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <boost/timer.hpp>

using namespace std;

#define N 10000
map<int, string> g_data;
const string filename = "test.txt";

void initData()
{
    for (int i = 0; i < N; ++i)
    {
        g_data.insert(make_pair(i, to_string(i) + "\n"));
    }
}

void createFile()
{
    ofstream f(filename);
    if (!f.is_open())
    {
        return;
    }

    for (auto it = g_data.cbegin(); it != g_data.cend(); ++it)
    {
        const string& str = it->second;
        f.write(str.c_str(), str.size());
    }
    f.close();
}

int main()
{
    initData();

    cout << "Hello World" << endl;
    system("pause");
    return 0;
}