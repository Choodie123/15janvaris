
try:
    f = open('text.txt', 'r', encoding='utf8')
except FileNotFoundError:
    print('files netika atrasts')

print(f.read())