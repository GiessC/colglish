"""
Author: Collin Giess
Project: colglish
File: error.py
Description: File containing the Error class for the colglish programming language
"""
from lexer.position import Position


class Error:
    """
    A class to represent an error
    """
    pos_start: Position
    pos_end: Position
    error_name: str
    details: str

    def __init__(self, pos_start: Position, pos_end: Position, error_name: str, details: str):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self) -> str:
        """
        Get the error as a string

        Returns:
            str: The error as a string
        """
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.filename}, line {self.pos_start.line_number + 1}'
        return result

    def __repr__(self) -> str:
        """
        Get the error as a string

        Returns:
            str: The error as a string
        """
        return self.as_string()

    def __str__(self) -> str:
        """
        Get the error as a string

        Returns:
            str: The error as a string
        """
        return self.as_string()
