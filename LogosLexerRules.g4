lexer grammar LogosLexerRules;


// ID
ID  : ID_LETER (ID_LETER | DIGIT)*;

// Numbers
INT     : '0' 'x' HEXDIGIT+
        | '0' 'b' BINDIGIT+
        | DIGIT+ ;
FLOAT   : DIGIT+ '.' DIGIT*
        | '.' DIGIT+
        ;

// Strings
STRING  : '"' ( ESC | .)*? '"'; // Notice the non-greedy notation *?

// Comments
COMMENT : '//' .*? '\n' -> skip;
// COMMENT_BLOCK        : '/*' .*? '*/' -> skip;

// Whitespaces
WS      : [ \t\n\r]+ -> skip;

// Operators
OP_ADD  : '+' ;
OP_SUB  : '-' ;
OP_MUL  : '*' ;
OP_DIV  : '/' ;
OP_EQ   : '==' ;
OP_NEQ  : '!=' ;
OP_GT    : '>' ;
OP_GEQ   : '>=' ;
OP_LT    : '<' ;
OP_LEQ   : '<=' ;
OP_AND   : '&' ;
OP_XOR  : '^' ;
OP_OR   : '|' ;
OP_LOGICAL_OR : '||' ;
OP_LOGICAL_AND : '&&' ;

// Fragments
fragment DIGIT      : '0'..'9';
fragment HEXDIGIT   : 'a'..'f' | 'A'..'F' | DIGIT;
fragment BINDIGIT   : '0' | '1';
fragment ID_LETER   : 'a'..'z' | 'A'..'Z' | '_';
fragment ESC        : '\\' [btnr"\\] ; // Escape sequences, such as \b, \t, \n etc.
