import pandas as pd
import collections

'''
PAYERACCOUNTNUMBER - номер счета плательщика
PAYEEACCOUNTNUMBER - номер счета получателя
AMOUNT - сумма операции
DATEIN - дата операции
'''

PAYER = []#массив счетов плательщика
sum_PAYER = collections.defaultdict(dict)

PAYEE = []#массив счетов получателя
sum_PAYEE = collections.defaultdict(dict)

loaded_table = pd.read_csv('Test_data.csv',sep=';') # читаем таблицу, с помощью параметра sep делим таблицу.

loaded_dict_PAYER = loaded_table['PAYERACCOUNTNUMBER'].to_dict()#преобразуем столбец  PAYERACCOUNTNUMBER в словарь
loaded_dict_PAYEE = loaded_table['PAYEEACCOUNTNUMBER'].to_dict()#преобразуем столбец PAYEEACCOUNTNUMBER в словарь
loaded_dict_AMOUNT = loaded_table['AMOUNT'].to_dict()

for count in range(len(loaded_dict_PAYER)):
    PAYER.append(loaded_dict_PAYER[count])
    PAYEE.append(loaded_dict_PAYEE[count])

PAYER = set(PAYER)# с помощью функции set убираем дубликаты счетов плательщика
PAYEE = set(PAYEE)# с помощью функции set убираем дубликаты счетов получателя

for count in range(len(loaded_dict_PAYER)):
    for number in PAYER:
        if loaded_dict_PAYER[count] == number:
            sum_PAYER.setdefault(number, []).append(float(loaded_dict_AMOUNT[count].replace(',','.')))

for key in sum_PAYER:
    sum_PAYER[key] = sum(sum_PAYER[key])

print(sum_PAYER)

print('Всего плательщиков: '+str(len(PAYER))+'\n'+'Всего получателей: ' + str(len(PAYEE)))