# 1000 -> 0
# 423 -> 8
# 1 -> 1

import string
user_inpute = int(input("Введите любое целое число:"))
x = 1
while user_inpute >= 9:
    x = 1
    while user_inpute > 0:
        digit = user_inpute % 10
        x *= digit
        user_inpute //= 10
    user_inpute = x
print(user_inpute)
