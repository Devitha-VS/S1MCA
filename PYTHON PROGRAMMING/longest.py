words=input("Enter the words separated by spaces:").split(',')
max_length=0
long_word=""
for word in words:
    if len(word)>max_length:
        max_length=len(word)
        long_word=word
print("longest word:",long_word)
print("Length of longest word:",max_length)
