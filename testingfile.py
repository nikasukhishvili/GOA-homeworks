def manual_count(lst, element):
    count = 0
    
    if element in lst:
        for item in lst:
            if item == element:
                count += 1
                
    return count

print(manual_count([-10, 11, 10, 10], -10))

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item != unique_list:
            unique_list.append(item)
        else:
            break
    return unique_list

print(remove_duplicates(['gela', "Gela", 'gela', 'luka']))