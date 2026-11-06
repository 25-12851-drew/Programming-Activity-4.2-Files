sentence = input("Sentence: ")

count = 0

for letter in sentence:
    if letter.lower() in "aeiou":
        count += 1

print("Vowels:", count)