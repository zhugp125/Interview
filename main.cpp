// g++ main.cpp -I/usr/local/include

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <boost/timer.hpp>

using namespace std;
using namespace boost;

#define N 1000000
#define COL 10
map<int, string> g_data;
const string filename = "test.txt";

void initData()
{
    for (int i = 0; i < N; ++i)
    {
        const string str = to_string(i);
        string s;
        for (int j = 0; j < COL - 1; ++j)
        {
            s += str + ' ';
        }
        s += str + '\n';
        g_data.insert(make_pair(i, s));
    }
}

void createFile()
{
    ofstream f(filename);
    if (!f.is_open())
    {
        return;
    }

    for (map<int, string>::const_iterator it = g_data.begin(); it != g_data.end(); ++it)
    {
        const string& str = it->second;
        f.write(str.c_str(), str.size());
    }
    f.close();
}

int main()
{
    timer t;
    initData();
    cout << "init date elapsed " << t.elapsed() << "s time\n"; //2.01548s

    t.restart();
    createFile();
    cout << "create file elapsed " << t.elapsed() << "s time\n"; //0.145693  84MB

    cout << "Hello World" << endl;
#ifdef _WIN32
    system("pause");
#endif
    return 0;
}
