%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char *s) { fprintf(stderr, "Error: %s\n", s); }
%}

%token IDENTIFIER VARIABLE ARROW LPAREN RPAREN QMARK EXCLAM DOT
%union {
    char *str;
    // other types
}

%%

action     : IDENTIFIER ARROW expr DOT ;
expr       : expr fn_call | fn_call | or_stop ;
or_stop    : fn_call QMARK fn_call | fn_call EXCLAM fn_call ;
fn_call    : IDENTIFIER | IDENTIFIER LPAREN arguments RPAREN ;
fn         : IDENTIFIER LPAREN arguments RPAREN ARROW fexpr DOT
           | IDENTIFIER ARROW fexpr DOT ;
fexpr      : expr fexpr | expr | literal ;
arguments  : VARIABLE | arguments VARIABLE ;
literal    : string | number | bool ;

string     : /* string rule */
bool       : /* bool rule */
number     : /* number rule */

%%

int main() {
   if (yyparse()) {
       fprintf(stderr, "Parsing failed\n");
   }
   return 0;
}
