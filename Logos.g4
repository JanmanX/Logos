grammar Logos;

prog: stmt+ EOF;

stmt : ID ':=' expr                 #assign
    | 'print' ID                    #print      
    | 'if' expr 'then' stmt         #if
    | 'exit' ID                     #exit
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