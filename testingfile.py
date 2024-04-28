def manual_count(lst, element):
    count = 0
    
    if element in lst:
        for item in lst:
            if item == element:
                count += 1
                
    return count

print(manual_count([10, 11, 10, 10], ))