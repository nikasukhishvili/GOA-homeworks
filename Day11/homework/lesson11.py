values = ['apple', 'banana', 'orange', 'grape', 'pineapple']
for i in range(len(values)):
    extracted = values.pop(0)
    replaced = 'new_' + extracted
    print(f"Extracted value: {extracted}")
    print(f"Replaced value: {replaced}")
    values.append(replaced)
    print("Updated list:", values)
