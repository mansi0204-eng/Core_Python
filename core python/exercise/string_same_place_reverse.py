name="mansi kumawat"
words=name.split()

for word in words:
    reverse_word=""
    for char in word:
        reverse_word=char+reverse_word
    print(reverse_word, end=" ")

