grammar Logos;

import LogosLexerRules;

prog: rituals+ EOF;

rituals: 'ritual' name=ID '(' args=ids? ')' '{' stmts+=stmt* '}'     #ritual
    ;

stmt: ID '=' expr                               #assign
    | ID '=' 'alloc' size=INT                   #allocMem
    | '[' ID ']' '=' value=expr                 #writeMem 
    | dest=ID '=' '[' source=ID ']'            #readMem
    | 'if' expr '{' stmts+=stmt* '}'            #if
    | 'while' expr '{' stmts+=stmt* '}'         #while
    | 'end' expr                                #return
   ;

ids : ID (',' ID)*;

exprs: expr (',' expr)*;

expr: left=expr op=(OP_MUL|OP_DIV) right=expr                       # MulDiv
    | left=expr op=(OP_ADD|OP_SUB) right=expr                       # AddSub
    | left=expr op=(OP_LT | OP_LEQ | OP_GT | OP_GEQ) right=expr     # LtLeqGtGeq
    | left=expr op=(OP_EQ  | OP_NEQ) right=expr                     # EqNeq 
    | left=expr op=(OP_AND | OP_XOR | OP_OR) right=expr             # AndXorOr  
    | left=expr op=(OP_LOGICAL_AND | OP_LOGICAL_OR) right=expr      # LogicalAndOr  
    | func=ID '(' args=exprs? ')'                                   # call
    | ID                                                            # Id                            
    | INT                                                           # Int
    ;
    