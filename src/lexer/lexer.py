"""
Author: Collin Giess
Project: colglish
File: lexer.py
Description: File containing the Lexer class for the colglish programming language
"""
from errors.types import IllegalCharError
from lexer.tokens.const import (DIGITS, TT_ASSIGN, TT_DIV, TT_FLOAT, TT_INT,
                          TT_MINUS, TT_MUL, TT_PLUS)
from lexer.tokens.types import Token
from errors.error import Error
from lexer.position import Position



class Lexer:
    """
    Lexer that reads through the source code and creates tokens
    """
    text: str
    pos: Position
    current_char: str | None

    def __init__(self, filename: str, text: str):
        self.fn = filename
        self.text = text
        self.pos = Position(-1, 0, -1, filename, text)
        self.current_char = None
        self.advance()

    def advance(self):
        """
        Advance the lexer to the next character
        """
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_tokens(self) -> tuple[list[Token], IllegalCharError]:
        """
        Make tokens from the source code

        Returns:
            list[Token]: List of tokens from the source code
        """
        tokens = []

        while self.current_char is not None:
            if self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '=':
                tokens.append(Token(TT_ASSIGN))
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            else:
                pos_start = self.pos.clone()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
        return tokens, None

    def make_number(self) -> Token:
        """
        Makes a number by reading the source code character by character

        Returns:
            Token: a token representing a number
        """
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        return Token(TT_FLOAT, float(num_str))


def run_lexer(filename: str, text: str) -> tuple[list[Token], Error | None]:
    """
    Runs the lexer

    Args:
        filename (str): The name of the file
        text (str): The source code

    Returns:
        tuple[list[Token], Error | None]: 
            the list of tokens from the source code
            and an error if there is one
    """
    lexer = Lexer(filename, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
