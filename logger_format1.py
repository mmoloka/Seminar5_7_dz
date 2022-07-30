from view import get_data as gt


def log_format1():
    data = open('log_format1.txt', 'a')
    data.write(gt('фамилию: '))
    data.write('\n')
    data.write('\n')
    data.write(gt('имя: '))
    data.write('\n')
    data.write('\n')
    data.write(gt('телефон: '))
    data.write('\n')
    data.write('\n')
    data.write(gt('описание: '))
    data.write('\n')
    data.write('\n')