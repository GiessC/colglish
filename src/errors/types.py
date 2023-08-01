"""
Author: Collin Giess
Project: colglish
File: types.py
Description: Contains the types of errors used in the colglish programming language
"""
from errors.error import Error
from lexer.position import Position

class IllegalCharError(Error):
    """
    An error for an illegal character    
    """
    def __init__(self, pos_start: Position, pos_end: Position, details: str):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)
