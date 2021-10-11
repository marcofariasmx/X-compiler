import ply.lex as lex

class MyLexer(object):

    # Key words
    def __init__(self):
        self.keywords = {
            'program': 'PROGRAM',
            'print': 'PRINT',
            'if': 'IF',
            'else': 'ELSE',
            'var': 'VAR',
            'int': 'INT',
            'float': 'FLOAT'

    }

    # Tokens based on the parser

    tokens = ['SEMICOLON', 'LEFTBRACKET', 'RIGHTBRACKET', 'GREATER', 'LESS', 'NOTEQUAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
            'LEFTPAREN', 'RIGHTPAREN', 'ID', 'CTEI', 'CTEF', 'COLON', 'EQUALS', 'CTESTRING', 'COMMA', 'PROGRAM', 'PRINT',
            'IF', 'ELSE', 'VAR', 'INT', 'FLOAT']

    # Regular expressions

    t_SEMICOLON = r'\;'
    t_LEFTBRACKET = r'\{'
    t_RIGHTBRACKET = r'\}'
    t_GREATER = r'>'
    t_LESS = r'<'
    t_NOTEQUAL = r'<>'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'\/'
    t_LEFTPAREN = r'\('
    t_RIGHTPAREN = r'\)'
    t_COLON = r':'
    t_EQUALS = r'\='
    t_CTESTRING = r'\".*\"'
    t_COMMA = r'\,'
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'


    # Regular expression with some action

    # Define an ID
    def t_ID(self,t):
        r'[A-za-z]([A-za-z]|[0-9])*'
        if t.value in self.keywords:
            t.type = self.keywords.get(t.value, 'ID')
        return t


    # Define a float number
    def t_CTEF(self,t):
        r'[0-9]*\.[0-9]+|[0-9]+'
        t.value = float(t.value)
        return t


    # Define a variable int
    def t_CTEI(self,t):
        r'[1-9][0-9]*'
        t.value = int(t.value)
        return t


    # Define a new line or multiple new lines
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    # Define a comment
    def t_comment(self,t):
        r'\%%.*'
        pass


    def t_error(self,t):
        print("Lexical error ' {0} ' found in line ' {1} ' ".format(t.value[0], t.lineno))
        t.lexer.skip(1)

     
     # Test its output
    def test(self,data):
        self.lexer.input(data)
        self.lexer.lineno = 1
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            print(tok)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        
        return self.lexer