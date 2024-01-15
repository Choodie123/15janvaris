
try:
    file = open('text.txt', 'r', encoding='utf8')
except FileNotFoundError:
    print('files netika atrasts')
rinda = file.readlines()

for i in rinda:
    file.read(rinda(2))