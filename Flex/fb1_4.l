%{
    enum yytokentype{
        NUMBER = 258,
        ADD = 259,
        SUB = 260,
        MUL = 261,
        DIV = 262,
        ABS = 263,
        EOL = 264
    };
    int yyval;
%}

%%
"+"   { return ADD; }
"-"   { return SUB; }
"*"   { return MUL; }
"/"   { return DIV; }
"|"   { return ABS; }
[0-9]+ { yyval = atoi(yytext); return NUMBER; }
\n    { return EOL; }
[ \t ]    { /* 忽略空白字符*/ }
.    { printf("Mystery character %c\n", *yytext); }
%%

int main(int argv, char** argc)
{
    int token;

    while(token = yylex()) {
        printf("%d", token);
        if (NUMBER == token)
        {
            printf(" = %d\n", yyval);
        }
        else
        {
            printf("\n");
        }
    }
    return 0;
}
