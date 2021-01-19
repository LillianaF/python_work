import math
'''with open('caged_bird.txt') as file_object:
    contents = file_object.read()
print(contents)
word = input("Enter a word to search for: ")
print(contents.lower().count(word))'''

wordList = ['laugh', 'Lord', 'family', 'school',
            'church', 'mother', 'Momma', 'Willie', 'Bailey', 'bird']
for word in wordList:
    with open('caged_bird.txt') as file_object:
        contents = file_object.read().lower()
        words = contents.split()
        # how so it searches regardless of capitalization
        times = contents.count(word)
        max_len = len(max(words, key=len))
        long = [word for word in words if len(word) == max_len]
        print(f"The word {word} appears {times} times.")

print(f"The longest word is {long}")
with open('caged_bird.txt') as file_object:
    lines = file_object.readlines()
print(
    f"The file caged_bird has {len(lines)} lines and {len(words)} words. There are about {round(len(words)/36)} words per chapter")
