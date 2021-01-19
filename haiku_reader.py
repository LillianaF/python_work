wordsList = []
with open('haiku.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        words = line.split()
        wordsList.append(words)
        print(len(words))
    print(len(lines))
print(wordsList)

with open('haiku.txt') as file_object:
    contents = file_object.read()
print(contents)
word = input("Enter a word to search for: ")
print(contents.lower().count(word))
