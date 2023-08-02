# reserved_words = [
#     'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
#     'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
#     'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
#     'try', 'while', 'with', 'yield'
# ]


import keyword
import string

while True:
    user_input = input("Введите имя переменной: ")
    name = user_input.strip('_')
    is_valid = True
    if not user_input[0].isalpha() and not user_input.startswith('_'):
        is_valid = False
    allowed_chars = '_0123456789' + string.ascii_lowercase
    if not all(char in allowed_chars for char in name):
        is_valid = False
    if name in keyword.kwlist:
        is_valid = False
    print("Результат:", is_valid)
