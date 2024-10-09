import json
from typing import Any, Dict, List

class Instruction:
    def __init__(self, instr: Dict[str, Any]):
        self.instr = instr
        self.op = instr.get('op')
        self.args = instr.get('args', [])
        self.dest = instr.get('dest')
        self.type = instr.get('type')
        self.labels = instr.get('labels', [])
        self.label = instr.get('label')

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