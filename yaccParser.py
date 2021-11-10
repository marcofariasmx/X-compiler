import ply.yacc as yacc

from lexer import MyLexer

from FuncsDir_Vars_Table import FuncsDir_Vars_Table

from collections import defaultdict

class MyParser(object):

    tokens = MyLexer.tokens

    def __init__(self):
    
        #Create DirFunc
        self.dirTable = FuncsDir_Vars_Table()

        # Build the parser and lexer
        self.lexer = MyLexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=self)

        #Create some helpers to store data
        self.varType = ''
        self.varNames = []
        #self.declaredVars = {'name': [], 'type': []}
        self.declaredVars = defaultdict(list)
        self.currScope = ''
        self.ownerFunc = ''

    #Helper functions
    def storeDeclaredVars(self):
        #print(self.varNames)
        #print(self.declaredVars)
        for var in self.varNames:
            self.declaredVars['name'].append(var)
            self.declaredVars['type'].append(self.varType)
        self.varNames.clear()
        self.varType = ''

    def insertVars(self):
        for var in self.declaredVars['name']:
            self.dirTable.insertVariable(var, self.declaredVars['type'][0], self.ownerFunc, self.currScope)
        self.declaredVars.clear()

    # Grammar declaration

    def p_program(self, p):
        '''program      :  PROGRAM program_id SEMICOLON globalVars globalFuncs MAIN LEFTPAREN RIGHTPAREN body
        '''

        print("-----p_program------")
        print(*p)

        p[0] = "COMPILED"

        self.ownerFunc = 'main'
        self.insertVars()

        print(self.varNames)
        print(self.varType)

    def p_expression_program_id(self, p):
        '''
        program_id : ID
        '''

        print("-----p_expression_program_id------")
        print(*p)
        self.ownerFunc = p[1]

        #Add id-name and type program a DirFunc
        self.dirTable.insertFunction(p[1], 'program', 1, None, None)

    def p_globalVars(self, p):
        '''
            globalVars  :  vars
                        |  empty 
        '''
        print("-----p_globalVars------")
        print(*p)
        self.currScope = 'global'
        #*#*#*#*#
        self.insertVars()

    def p_globaFuncs(self, p):
        '''
            globalFuncs :  functions
                        |  empty
        '''
        print("-----p_globaFuncs------")
        print(*p)
        self.currScope = 'local'
        self.insertVars()

    def p_vars(self, p):
        ''' 
            vars    :  VARS type_simple multiVar SEMICOLON
        '''
        print("----VARS-----")
        print(*p)
        
        self.storeDeclaredVars()

        ########

        #If current Func doesn’t have a VarTable then Create VarTable and link it to current Func
        #if p[1] == 'vars':
        #    for var in self.varNames:
        #        self.dirTable.insertVariable(var, self.varType[0], self.currScope)
        #    self.varType.clear()
        #    self.varNames.clear()

    def p_singleVar(self, p):
        ''' 
            singleVar  :  variable
        '''
        print("----p_singleVar-----")
        print(*p)

    def p_multiVar(self, p):
        ''' 
            multiVar    :   singleVar COMMA multiVar
                        |   singleVar 
        '''
        print("----p_multiVar-----")
        print(*p)

    def p_functions(self, p):
        ''' functions    :   FUNC functionType
            functionType :   type_simple function_id LEFTPAREN params RIGHTPAREN body_return
                         |   VOID ID LEFTPAREN RIGHTPAREN body
        '''
        print("-----FUNCTIONS------")
        print(*p)

        #Add id-name and type program a DirFunc
        if p[1] and p[2]:
            self.dirTable.insertFunction(p[2], p[1], 1, None, None)
            self.ownerFunc = p[2]


    def p_expression_function_id(self, p):
        '''
        function_id : ID
        '''

        #Add id-name and type program a DirFunc
        print("-----function_id------")
        print(*p)


    def p_type_simple(self, p):
        ''' type_simple :   INT
                        |   FLOAT
                        |   CHAR
        '''
        print("-----TYPE SIMPLE------")
        print(*p)
        self.varType = p[1]
        
    def p_variable(self, p):
        ''' variable    :   ID
                        |   ID LEFTSQBRACKET exp RIGHTSQBRACKET
                        |   ID LEFTSQBRACKET exp RIGHTSQBRACKET LEFTSQBRACKET exp RIGHTSQBRACKET
        '''

        print("-----VARIABLE------")
        print(*p)
        self.varNames.append(p[1])

    def p_params(self, p):
        ''' params  :   type_simple ID
                    |   type_simple ID COMMA params
        '''
        
    def p_body(self, p):
        ''' 
            body    :   LEFTBRACKET bodyContent RIGHTBRACKET
        '''
        print("-----p_body------")
        print(*p)

    def p_bodyContent(self, p):
        ''' bodyContent :   statute bodyContent
                        |   empty
        '''
        print("-----p_bodyContent------")
        print(*p)

    def p_body_return(self, p):
        ''' 
            body_return :   LEFTBRACKET bodyContent_return RETURN factor RIGHTBRACKET
        '''
        print("-----p_body_return------")
        print(*p)

    def p_bodyContent_return(self, p):
        ''' bodyContent_return  :   statute bodyContent_return
                                |   empty
        '''
        print("-----p_bodyContent_return------")
        print(*p)

    def p_call(self, p):
        ''' call    :   ID LEFTPAREN call1 RIGHTPAREN
            call1   :   exp
                    |   exp COMMA call1
        '''
        print("-----p_call------")
        print(*p)

    def p_statute(self, p):
        '''statute  :   vars
                    |   assignment
                    |   write
                    |   read
                    |   if
                    |   for
                    |   while
                    |   call
        '''
        print("-----p_statute------")
        print(*p)


    def p_assignment(self, p):
        '''assignment :     ID ASSIGNMENT expression SEMICOLON
        '''

        print("-----p_assignment------")
        print(*p)

    ########## review cte_string
    def p_write(self, p):
        '''write  :   PRINT LEFTPAREN write1 RIGHTPAREN SEMICOLON
        write1 :   expression COMMA write1
                |   expression
        '''

        print("-----p_write------")
        print(*p)

    def p_read(self, p):
        '''read  :   READ LEFTPAREN read1 RIGHTPAREN SEMICOLON
        read1 :   variable 
                |   variable read2
        read2 :   COMMA read1 
        '''

        print("-----p_read------")
        print(*p)

    def p_if(self, p):
        '''if  :   IF LEFTPAREN expression RIGHTPAREN body if1
        if1 :   ELSE body
            |   empty
        '''

        print("-----p_if------")
        print(*p)

    def p_for(self, p):
        '''for  :   FOR LEFTPAREN expression TO factor RIGHTPAREN body
        '''

        print("-----p_for------")
        print(*p)

    def p_while(self, p):
        '''while  :   WHILE LEFTPAREN expression RIGHTPAREN body
        '''

        print("-----p_while------")
        print(*p)

    def p_expression(self, p):
        ''' expression  :   exp
                        |   exp GREATER exp
                        |   exp LESS exp
                        |   exp NOTEQUAL exp
                        |   exp EQUAL exp
        '''

        print("-----p_expression------")
        print(*p)


    def p_exp(self, p):
        ''' exp :   term
                |   term PLUS exp
                |   term MINUS exp
        '''

        print("-----p_exp------")
        print(*p)

    def p_term(self,p):
        '''term  :   factor
                |   factor TIMES term
                |   factor DIVIDE term   
        '''

        print("-----p_term------")
        print(*p)

    def p_factor(self,p):
        '''factor :   LEFTPAREN exp RIGHTPAREN
                |   CTE_I
                |   CTE_F
                |   CTE_CH
                |   variable
                |   CALL
        '''

        print("-----p_factor------")
        print(*p)

    # Error rule for syntax errors
    def p_error(self,p):
        print("Syntax error in input! - {} ".format(p))


    def p_empty(self, p):
        '''empty :'''
        pass



#####DEBUGS:

# 1) Resolver lo de CTE_String y CTE_CH
# 2) Al haberlo resuelto, cambiar la gramática para que incluya comillas y se de a entender que eso es el string o char