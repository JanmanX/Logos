grammar Logos;

import LogosLexerRules;

prog: stmt+ EOF;

stmt: ID '=' expr                               #assign
    | ID '=' 'alloc' size=INT                   #allocMem
    | ID '[' index=expr ']' '=' value=expr      #writeMem
    | dest=ID '=' source=ID '[' index=expr ']'  #readMem
    | 'if' expr '{' stmts+=stmt* '}'            #if
    | 'while' expr '{' stmts+=stmt* '}'         #while
    | 'include' path=STRING                     #include
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
    