grammar Logos;

import LogosLexerRules;

prog: stmt+ EOF;

stmt: ID '=' expr                   #assign
    | 'mem' size=INT ID             #assignMem
    | 'print' ID                    #print      
    | 'if' expr 'then' stmt         #if
    | 'exit' ID                     #exit
    ;

expr: left=expr op=(OP_MUL|OP_DIV) right=expr                       # MulDiv
    | left=expr op=(OP_ADD|OP_SUB) right=expr                       # AddSub
    | left=expr op=(OP_LT | OP_LEQ | OP_GT | OP_GEQ) right=expr     # LeLeqGeGeq
    | left=expr op=(OP_EQ  | OP_NEQ) right=expr                     # EqNeq 
    | left=expr op=(OP_AND | OP_XOR | OP_OR) right=expr             # AndXorOr  
    | left=expr op=(OP_LOGICAL_AND | OP_LOGICAL_OR) right=expr      # LogicalAndOr  
    | ID                                                            # Id                            
    | INT                                                           # Int
    ;

ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;