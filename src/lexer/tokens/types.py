"""
Author: Collin Giess
Project: colglish
File: types.py
Description: Token class for lexer
"""
class Token:
    """
    Token class for lexer
    """
    def __init__(self, type_: str, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
