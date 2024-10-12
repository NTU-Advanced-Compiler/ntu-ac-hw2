import json
from typing import Any, Dict, List

class Instruction:
    def __init__(self, instr: Dict[str, Any]):
        self.instr = instr
        self._op = instr.get('op')
        self._args = instr.get('args', [])
        self._dest = instr.get('dest')
        self._type = instr.get('type')
        self._funcs = instr.get('funcs', [])
        self._labels = instr.get('labels', [])
        self._label = instr.get('label')
        self._value = instr.get('value')

    def __repr__(self):
        return json.dumps(self.instr)

class Function:
    def __init__(self, func: Dict[str, Any]):
        self.name = func['name']
        self.args = func.get('args', [])
        self.instrs = [Instruction(instr) for instr in func['instrs']]

    def to_dict(self):
        return {
            'name': self.name,
            'args': self.args,
            'instrs': [instr.instr for instr in self.instrs]
        }

class Program:
    def __init__(self, prog: Dict[str, Any]):
        self.functions = [Function(func) for func in prog['functions']]

    def to_dict(self):
        return {
            'functions': [func.to_dict() for func in self.functions]
        }

def parse_bril(json_str: str) -> Program:
    prog = json.loads(json_str)
    return Program(prog)

def serialize_bril(prog: Program) -> str:
    return json.dumps(prog.to_dict(), indent=2)