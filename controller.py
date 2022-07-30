import view as v
import logger_format1 as lf1
import logger_format2 as lf2


def choose_act(data):
    if data == '1':
        lf1.log_format1()
    if data == '2':    
        lf2.log_format2()
    if data == '11':
        for line in open('log_format1.txt', 'r'):
            v.view_data(line)
    if data == '12':
        for line in open('log_format2.txt', 'r'):
            v.view_data(line)

def input_act():
    return v.get_data('\n1- для записи данных в формате 1,\n'
                '2- для записи данных в формате 2\n'
                '11- для экспорта данных в формате 1\n'
                '12- для экспорта данных в формате 2\n')


