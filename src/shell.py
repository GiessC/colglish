"""
Runs a shell for the language
"""
from lexer.lexer import run_lexer


def run_shell():
    """
    Run the shell
    """
    while True:
        text = input('>>> ')
        result, error = run_lexer('<stdin>', text)

        if error:
            print(error)
        else:
            print(result)

if __name__ == '__main__':
    run_shell()
