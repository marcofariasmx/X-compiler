class FuncsDir_Vars_Table():

    def __init__(self) -> None:
        self.FuncsDirectory = {'name': [], 'type': [], 'initDirection': [], 'size': [], 'parameters' : {'paramType': [], 'paramVarName': []}}

        self.VarsDirectory = {'name': [], 'type': [], 'ownerFunc': [], 'scope': []}

    def insertFunction(self, funcName, funcType, initDirection, size, parameters):
        self.FuncsDirectory['name'].append(funcName)
        self.FuncsDirectory['type'].append(funcType)
        self.FuncsDirectory['initDirection'].append(initDirection)
        self.FuncsDirectory['size'].append(size)

        if parameters:
            for param in parameters:
                self.FuncsDirectory['parameters']['paramType'].append(param['paramType'])
                self.FuncsDirectory['parameters']['paramVarName'].append(param['paramVarName'])
        else:
            self.FuncsDirectory['parameters']['paramType'].append(None)
            self.FuncsDirectory['parameters']['paramVarName'].append(None)

        print(self.FuncsDirectory)
    
    def insertVariable(self, varName, varType, ownerFunc, scope):
        self.VarsDirectory['name'].append(varName)
        self.VarsDirectory['type'].append(varType)
        self.VarsDirectory['ownerFunc'].append(ownerFunc)
        self.VarsDirectory['scope'].append(scope)

        print(self.VarsDirectory)

    def action(self):
        return None
