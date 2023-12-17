%{
#include "g.tab.h"
%}

%%

"true" | "false"                { /* handle boolean */ }
[a-z][a-zA-Z0-9\-]*[a-z0-9]     { yylval.str = strdup(yytext); return IDENTIFIER; }
[A-Z][a-zA-Z0-9\-]*[a-z0-9]     { yylval.str = strdup(yytext); return VARIABLE; }
"->"                            { return ARROW; }
"("                             { return LPAREN; }
")"                             { return RPAREN; }
"?"                             { return QMARK; }
"!"                             { return EXCLAM; }
"."                             { return DOT; }
"\""                            { /* handle string */ }
[0-9]+                          { /* handle number */ }
\n | [ \t]                      { /* ignore whitespace */ }
.                               { /* handle other characters */ }

%%
