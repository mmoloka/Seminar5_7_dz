from view import get_data as gt

def log_format2():
    data = open('log_format2.txt', 'a')
    data.write(gt('фамилию: '))
    data.write(', ')
    data.write(gt('имя: '))
    data.write(', ')
    data.write(gt('телефон: '))
    data.write(', ')
    data.write(gt('описание: '))
    data.write('\n')