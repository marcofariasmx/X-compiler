class memory():

    def __init__(self) -> None:
        
        self.globalMem = {'operator': [], 'operand1': [], 'operand2': [], 'result': []}
        self.localMem = {'operator': [], 'operand1': [], 'operand2': [], 'result': []}
        self.tempMem = {'operator': [], 'operand1': [], 'operand2': [], 'result': []}
        self.constMem = {'operator': [], 'operand1': [], 'operand2': [], 'result': []}

    def action(self):
        return None
