/**
 *	@file   TLMd5.h
 *
 *  @brief  计算MD5
 *          http://files.cnblogs.com/flying_bat/md5.rar
 *
 *  @author zhangyi
 *
 *  @date   2011-12-15
 */

#ifndef UPDATER_UTIL_TLMD5_H
#define UPDATER_UTIL_TLMD5_H

#include <string>
#include <fstream>

/* Type define */
typedef unsigned char byte;
typedef unsigned long ulong;

using std::string;
using std::ifstream;


/* MD5 declaration. */
class MD5 {
public:
    MD5();
    MD5(const void *input, size_t length);
    MD5(const string &str);
    MD5(ifstream &in);
    void update(const void *input, size_t length);
    void update(const string &str);
    void update(ifstream &in);
    const byte* digest();
    string toString();
    void reset();
private:
    void update(const byte *input, size_t length);
    void final();
    void transform(const byte block[64]);
    void encode(const ulong *input, byte *output, size_t length);
    void decode(const byte *input, ulong *output, size_t length);
    string bytesToHexString(const byte *input, size_t length);

    /* class uncopyable */
    MD5(const MD5&);
    MD5& operator=(const MD5&);
private:
    ulong _state[4];	/* state (ABCD) */
    ulong _count[2];	/* number of bits, modulo 2^64 (low-order word first) */
    byte _buffer[64];	/* input buffer */
    byte _digest[16];	/* message digest */
    bool _finished;		/* calculate finished ? */

    static const byte PADDING[64];	/* padding for calculate */
    static const char HEX[16];
    static const size_t BUFFER_SIZE = 1024;
};

#endif/*MD5_H*/