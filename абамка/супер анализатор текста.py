text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

a = set(words)

longest_word = words[0]
smallest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(smallest_word):
        smallest_word = word

print('Количество разных слов:', len(a))
print('Самое длинное слово:', longest_word)
print("Самое короткое слово:", smallest_word)
print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")