%option noyywrap
%{
int chars = 0;
int words = 0;
int lines = 0;

int total_chars = 0;
int total_words = 0;
int total_lines = 0;
%}

%%

[a-zA-Z]+  { ++words; chars += strlen(yytext); }
\n         { ++chars; ++lines; }
.          { ++chars; }

%%

int main(int argc, char** argv)
{
    if (argc < 2) /* 读取标准输入 */
    {
        yylex();
        printf("%8d%8d%8d\n", lines, words, chars);
        return 0;
    }

    int i = 1;
    for (; i < argc; ++i)
    {
        FILE *f = fopen(argv[i], "r");
        if (!f)
        {
            perror(argv[i]);
            return 1;
        }

        yyrestart(f);
        yylex();
        fclose(f);
        printf("%8d%8d%8d %s\n", lines, words, chars, argv[i]);

        total_chars += chars;
        chars = 0;
        total_words += words;
        words = 0;
        total_lines += lines;
        lines = 0;
    }
    if (argc > 1)
    {
        printf("%8d%8d%8d\n", total_lines, total_words, total_chars);    
    }
    return 0;
}