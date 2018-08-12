%{
#include "fb1_5.tab.h"
%}

%%
"+"   { return ADD; }
"-"   { return SUB; }
"*"   { return MUL; }
"/"   { return DIV; }
"|"   { return ABS; }
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
\n    { return EOL; }
[ \t ]    { /* 忽略空白字符*/ }
.    { printf("Mystery character %c\n", *yytext); }
%%

