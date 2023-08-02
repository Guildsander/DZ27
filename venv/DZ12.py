
import string

input_string = input("Введіть рядок: ")
clean_string = ''.join(char for char in input_string if char not in string.punctuation)
words = clean_string.split()
capitalized_words = [word.capitalize() for word in words if word.isalpha()]
hashtag = '#' + ''.join(capitalized_words)
hashtag = hashtag[:140]
print("Хештег:", hashtag)



