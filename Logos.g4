grammar Logos;

prog: stmt+ EOF;

stmt : ID ':=' expr
    | 'print' expr
    ;

expr: expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | '(' expr ')'
    | ID
    | INT
    ;

ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;