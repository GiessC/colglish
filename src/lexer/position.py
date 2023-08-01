"""
Author: Collin Giess
Project: colglish
File: position.py
Description: 
"""
class Position:
    """
    A class to represent a position in the source code for the lexer
    """
    def __init__(self, index: int, line_number: int, col: int, filename: str, file_txt: str):
        self.index = index
        self.line_number = line_number
        self.col = col
        self.filename = filename
        self.file_txt = file_txt

    def advance(self, current_char: str | None):
        """
        Advances the position

        Args:
            current_char (str | None): The character at the current position
        """
        self.index += 1
        self.col += 1
        
        if current_char == '\n':
            self.line_number += 1
            self.col = 0
            
        return self
    
    def clone(self) -> 'Position':
        """
        Clones the position

        Returns:
            Position: The cloned position
        """
        return Position(self.index, self.line_number, self.col, self.filename, self.file_txt)
