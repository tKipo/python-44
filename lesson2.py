telephone_number = '+375299379992'

for elem in telephone_number:
    if elem == '+':
        continue
    if not elem.isdigit():
        print('ERROR')
        break
    print(elem, end=' ')
else:
    print('\nAll right')
