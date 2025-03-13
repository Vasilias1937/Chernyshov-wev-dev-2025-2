import string


with open('example.txt', 'r', encoding='utf-8') as file:
    text = file.read()


translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator)


words = cleaned_text.split()


max_length = max(len(word) for word in words)

longest_words = [word for word in words if len(word) == max_length]

print(longest_words)
