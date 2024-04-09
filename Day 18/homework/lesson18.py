word = str(input("Enter a word: "))
lowercase_word = str(input("enter lowercase: "))

if word.lower() == lowercase_word:
    print("both are correct")
else:
    print("both dont match")

word1 = input("Enter a word with uppercase letters only: ")
counter = 0
for char in word1:
    if char.islower():
        print("The word contains lowercase letters. try again.")
        counter = counter + 1
    else:

user_word = input("Please enter uppercase word: ")

result = ''

for index in range(len(user_word)):
    if index % 2 == 0:
        result = result + user_word[index].upper()
    else:
        result = result + user_word[index].lower()

print(result)