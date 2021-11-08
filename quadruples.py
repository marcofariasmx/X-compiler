class quadruples():

    def __init__(self) -> None:
        
        self.quadruples = {'operator': [], 'operand1': [], 'operand2': [], 'result': []}
        self.jumpStack = [] #to momentarily store jumps related to pending gotos

        self.operatorsStack = [] # +, -, *, /, >, <, etc
        self.operandsStack = {'operand': [], 'type': []} #operands: a, b, c.. types: int, char, bool...

    def action(self):
        return None
