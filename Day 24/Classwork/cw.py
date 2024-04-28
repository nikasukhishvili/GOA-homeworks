#kyu 8 
# first link
def litres(time):
    return time // 2

#second link
def paperwork(paper, classmates):
    if paper < 0 or classmates < 0:
        return 0
    return paper * classmates

#third link
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

#fourth link
def fake_bin(x)
    #cant do it yet

#fifth link
def count_by(given, multiple):
    numbers = []
    for i in range(0, multiple):
        numbers.append(given * i)
    return numbers

print(count_by(1, 10))