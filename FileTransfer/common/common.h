#ifndef COMMON_H
#define COMMON_H

#include "md5.h"
#include <fstream>

const char* g_separator = "#";
const char* g_sender_header_over = "reciver header done";
const char* g_sender_file_over = "write file done";

const char* g_config_path = "../common/config.ini";

std::string readFile(const std::string &fileName)
{
    std::ifstream f(fileName);
    return std::string((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
}

const std::string getMd5ByFile(const std::string &fileName)
{
    MD5 md5(readFile(fileName));
    return md5.md5();
}

#endif // COMMON_H
