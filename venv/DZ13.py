# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA


import string


input_string = input("Введите 2 буквы через дефиз:")
start_char, end_char = input_string.split('-')

start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char) + 1

result = string.ascii_letters[start_index:end_index]
print(result)
