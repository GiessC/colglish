"""
Author: Collin Giess
Project: colglish
File: aliases.py
Description: Contains aliases for various tokens for the lexer
"""
ALIASES = {
    '=': [
        'is',
        'set',
    ],
    '+': [
        'plus',
        'add',
    ],
    '-': [
        'minus',
        'subtract',
    ],
    '*': [
        'multiply',
        'times',
    ],
    '/': [
        'divided by',
        'divide',
        'over',
    ],
    '==': [
        'equals',
        'is equal to',
        'is equal',
    ],
    '!=': [
        'does not equal',
        'is not equal to',
        'is not equal',
    ],
    '<': [
        'less than',
        'is less than',
    ],
    '>': [
        'greater than',
        'is greater than',
    ],
    '<=': [
        'less than or equal to',
        'is less than or equal to',
    ],
    '>=': [
        'greater than or equal to',
        'is greater than or equal to',
    ],
    'and': [
        '&&',
        'also',
        'as well as',
    ],
    'or': [
        '||',
        'either',
    ],
    'not': [
        '!',
        'is not',
    ],
    'if': [
        'when',
    ],
    'else': [
        'otherwise',
    ],
    'elif': [
        'otherwise if',
        'otherwise when',
        'elwhen',
    ],
    'for': [],
    'while': [],
    'say': [
        'print',
        'speak',
        'output',
    ],
    'read': [
        'input',
    ],
}
