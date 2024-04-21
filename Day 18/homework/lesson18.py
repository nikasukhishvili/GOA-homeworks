name = str(input("Enter a name: "))
if name == name.lower():
    print("already in lowercase. nice")
else:
    print("it isnt in lowercase")

counter = 0
while True:
    word = str(input("Enter a word: "))
    counter += 1
    if any(letter.islower() for letter in word):
        print("You entered a word with lowercase letters. Please enter it again.")
    else:
        print("word entered:", word)
        print("number of tries", counter)
        break

word = input("Enter a word: ")
converted_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        converted_word += word[i].upper()
    else:
        converted_word += word[i].lower()
print("Converted word:", converted_word)


name = "sabashubashishvili"  
if len(name) > 5:
    converted_name = name.upper()
else:
    converted_name = name.lower()
print("Converted name:", converted_name)


names = ["saba", "shubashishvili"]
capitalized_names = [names.capitalize()]
print("Capitalized names:", capitalized_names)

# Outputting user's initials as a string:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
initials = first_name[0].capitalize() + "." + last_name[0].capitalize()
print("Initials:", initials)

# Printing index of the first letter in a word:
word = input("Enter a word: ")
search_letter = input("Enter the letter to search: ")
index = word.find(search_letter)
print("Index of the first letter:", index)

# Printing index of the first letter in a word using a loop:
word = input("Enter a word: ")
search_letter = input("Enter the letter to search: ")
index = -1
for i, letter in enumerate(word):
    if letter == search_letter:
        index = i
        break
print("Index of the first letter:", index)

# Concatenating family names with "-" separator:
family_members = ["John", "Doe", "Jane", "Smith"]  # Example family members
concatenated_names = "-".join(family_members)
print("Concatenated names:", concatenated_names)

# Joining even-indexed words with a matching value:
words = ["python", "html", "css", "js", "git"]  # Example words
value = input("Enter a value to join with even-indexed words: ")
joined_words = ""
for i, word in enumerate(words):
    if i % 2 == 0:
        joined_words += word + value
print("Joined words:", joined_words)
