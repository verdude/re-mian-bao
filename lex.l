%{
#include "g.tab.h"
%}

%%

"true" | "false"                { return BOOL }
[a-z][a-zA-Z0-9\-]*[a-z0-9]     { yylval.str = strdup(yytext); return IDENTIFIER; }
[A-Z][a-zA-Z0-9\-]*[a-z0-9]     { yylval.str = strdup(yytext); return VARIABLE; }
"->"                            { return ARROW; }
"("                             { return LPAREN; }
")"                             { return RPAREN; }
"?"                             { return QMARK; }
"!"                             { return EXCLAM; }
"."                             { return DOT; }
\"[^\"]*\"                      { yylval.str = strdup(yytext); return STRING; }
[0-9]+                          { yylval.num = atoi(yytext); return NUMBER; }
\n | [ \t]                      { }

%%
