def names():
    name = input('yo name here --> ')
    print('Capitalized:', name.capitalize())
    print('Upper case:', name.upper())
    print('Lower case:', name.lower())

names()

def find_index(word, letter):
    index = 0
    for i in word:
        if i == letter:
            return index
        index += 1

index = find_index("GOA", "A")
print("Index of ' ", index) 

def len(lst):
    count = 0
    for w in lst:
        count += 1

print('Amount of words in my list' , len(['goa', 'saba', 'gela']))