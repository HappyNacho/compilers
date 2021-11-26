import ply.lex as lex

reserved = {
    'and' : 'AND',
    'or' : 'OR',
    'if' : 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'boolean' : 'BOOLEAN',
    'float' : 'FLOAT',
    'int' : 'INT',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'print' : 'PRINT',
    'string' : 'STRING'
}

tokens = list(reserved.values()) + [
    'NUMI',
    'NUMF',
    'ID',
    'EQUALS',
    'NOTEQUALS',
    'GTREAQTHAN',
    'LSSEQTHAN'
]
literals = ['=', '+', '-', '*', '/', '^', '>', '<', '(', ')', '{', '}', ';']

t_EQUALS = r'=='
t_NOTEQUALS = r'!='
t_GTREAQTHAN = r'>='
t_LSSEQTHAN = r'<='
t_NUMI = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_NUMF = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
#t_STR = r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''

t_ignore = ' \t'

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved.get(t.value, "ID")
    return t

def t_error(t):
	print("Illegal character %s" % repr(t.value[0]))
	t.lexer.skip(1)

lx = lex.lex()