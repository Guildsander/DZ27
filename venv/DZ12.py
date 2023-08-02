import string
input_string = input("Введите строку: ")
clean_string = ''.join(char for char in input_string if char not in string.punctuation and char != ' ')
words = clean_string.split()
capitalized_words = [word.capitalize() for word in words]
hashtag = '#' + ''.join(capitalized_words)
hashtag = hashtag[:140]
print("Хэштег:", hashtag)
