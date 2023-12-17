%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char *s) { fprintf(stderr, "Error: %s\n", s); }
%}

%token IDENTIFIER VARIABLE ARROW LPAREN RPAREN QMARK EXCLAM DOT STRING BOOL NUMBER
%union {
    char *str;
    int num;
}

%%

fn         : IDENTIFIER LPAREN arguments RPAREN ARROW fexpr DOT
           | IDENTIFIER ARROW fexpr DOT ;
expr       : expr fn_call | fn_call | or_stop ;
fexpr      : expr fexpr | expr | literal ;
or_stop    : fn_call QMARK fn_call | fn_call EXCLAM fn_call ;
fn_call    : IDENTIFIER | IDENTIFIER LPAREN arguments RPAREN ;
arguments  : VARIABLE | arguments VARIABLE ;
literal    : string | number | bool ;

string     : STRING ;
bool       : BOOL ;
number     : NUMBER ;

%%

int main() {
   if (yyparse()) {
       fprintf(stderr, "Parsing failed\n");
   }
   return 0;
}
