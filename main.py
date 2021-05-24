import pandas as pd
import collections

'''
PAYERACCOUNTNUMBER - номер счета плательщика
PAYEEACCOUNTNUMBER - номер счета получателя
AMOUNT - сумма операции
DATEIN - дата операции
'''
def write_excel(array,name):
    data = [i for i in range(len(array))]
    table_taP = pd.DataFrame.from_dict(array, orient='index')
    writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
    table_taP.to_excel(writer, sheet_name='Factor_Table')
    writer.save()
    writer.close()
#Функция на подсчёт общий суммы операций
def total_amount(dicti,array):
    total_array = collections.defaultdict(dict)
    for count in range(len(dicti)):
        for number in array:
            if dicti[count] == number:
                total_array.setdefault(number, []).append(float(loaded_dict_AMOUNT[count].replace(',', '.')))
    for key in total_array:
        total_array[key] = str(sum(total_array[key]))
    return total_array

def max_amount(dicti,array):
    total_array = collections.defaultdict(dict)
    for count in range(len(dicti)):
        for number in array:
            if dicti[count] == number:
                total_array.setdefault(number, []).append(float(loaded_dict_AMOUNT[count].replace(',', '.')))
    for key in total_array:
        total_array[key] = str(max(total_array[key]))
    return total_array

#Функиця на подсчёт	общее количество операций
def total_operati(dicti,array):
    total_operatin = collections.defaultdict(dict)
    for number in array:
        total_operatin[number] = 0

    for count in range(len(dicti)):
        for number in array:
            if dicti[count] == number:
                total_operatin[number] = total_operatin[number] + 1
    return total_operatin

PAYER = []#массив счетов плательщика
PAYEE = []#массив счетов получателя
DATEIN=[]#массив для дат

tA_PAYER_PAYEE = collections.defaultdict(dict) #Общая сумма операций от плательщика x получателю y (для каждой пары плательщик-получатель)
tO_PAYER_PAYEE = collections.defaultdict(dict) #Общая количество операций от плательщика x получателю y (для каждой пары плательщик-получатель)

tA_PAYER_PAYEE_DATEIN = collections.defaultdict(dict)#Общая сумма операций от плательщика x получателю y за дату z (для каждой пары плательщик-получатель и каждой даты)
tO_PAYER_PAYEE_DATEIN = collections.defaultdict(dict)#Общая количество операций от плательщика x получателю y за дату z (для каждой пары плательщик-получатель и каждой даты)

loaded_table = pd.read_csv('Test_data.csv',sep=';') # читаем таблицу, с помощью параметра sep делим таблицу.

loaded_dict_PAYER = loaded_table['PAYERACCOUNTNUMBER'].to_dict()#преобразуем столбец  PAYERACCOUNTNUMBER в словарь
loaded_dict_PAYEE = loaded_table['PAYEEACCOUNTNUMBER'].to_dict()#преобразуем столбец PAYEEACCOUNTNUMBER в словарь
loaded_dict_AMOUNT = loaded_table['AMOUNT'].to_dict()#преобразуем столбец AMOUNT в словарь
loaded_dict_DATEIN = loaded_table['DATEIN'].to_dict()#преобразуем столбец DATEIN в словарь

#цикл на заполнение массивов
for count in range(len(loaded_dict_PAYER)):
    PAYER.append(loaded_dict_PAYER[count])
    PAYEE.append(loaded_dict_PAYEE[count])
    DATEIN.append(loaded_dict_DATEIN[count])
    tA_PAYER_PAYEE[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] = 0.0

    tA_PAYER_PAYEE_DATEIN[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] = {}
    tA_PAYER_PAYEE_DATEIN[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]][loaded_dict_DATEIN[count]] = 0.0

    tO_PAYER_PAYEE[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] = 0

    tO_PAYER_PAYEE_DATEIN[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] = {}
    tO_PAYER_PAYEE_DATEIN[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]][loaded_dict_DATEIN[count]] = 0

#цикл на подсчёт общей суммы операций от плательщика x получателю y (для каждой пары плательщик-получатель)
for count in range(len(loaded_dict_PAYER)):
    if loaded_dict_PAYER[count] in tA_PAYER_PAYEE and (loaded_dict_PAYEE[count]) in tA_PAYER_PAYEE[loaded_dict_PAYER[count]]:
        tA_PAYER_PAYEE[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] = tA_PAYER_PAYEE[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] + float(loaded_dict_AMOUNT[count].replace(',', '.'))

#цикл подсчёта Общая сумма операций от плательщика x получателю y за дату z (для каждой пары плательщик-получатель и каждой даты)
for count in range(len(loaded_dict_PAYER)):
    payer = loaded_dict_PAYER[count]
    payee = loaded_dict_PAYEE[count]
    datein = loaded_dict_DATEIN[count]
    if payer in tA_PAYER_PAYEE_DATEIN and payee in tA_PAYER_PAYEE_DATEIN[payer] and  datein in tA_PAYER_PAYEE_DATEIN[payer][payee]:
        tA_PAYER_PAYEE_DATEIN[payer][payee][datein] = tA_PAYER_PAYEE_DATEIN[payer][payee][datein] + float(loaded_dict_AMOUNT[count].replace(',', '.'))

#цикл на подсчётколичество операций от плательщика x получателю y (для каждой пары плательщик-получатель)
for count in range(len(loaded_dict_PAYER)):
    if loaded_dict_PAYER[count] in tO_PAYER_PAYEE and (loaded_dict_PAYEE[count]) in tO_PAYER_PAYEE[loaded_dict_PAYER[count]]:
            tO_PAYER_PAYEE[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] = tO_PAYER_PAYEE[loaded_dict_PAYER[count]][loaded_dict_PAYEE[count]] + 1

#цикл подсчёта общего количества операций от плательщика x получателю y за дату z (для каждой пары плательщик-получатель и каждой даты)
for count in range(len(loaded_dict_PAYER)):
    payer = loaded_dict_PAYER[count]
    payee = loaded_dict_PAYEE[count]
    datein = loaded_dict_DATEIN[count]
    if payer in tO_PAYER_PAYEE_DATEIN and payee in tO_PAYER_PAYEE_DATEIN[payer] and  datein in tO_PAYER_PAYEE_DATEIN[payer][payee]:
        tO_PAYER_PAYEE_DATEIN[payer][payee][datein] = tO_PAYER_PAYEE_DATEIN[payer][payee][datein] + 1

PAYER = set(PAYER)# с помощью функции set убираем дубликаты счетов плательщика
PAYEE = set(PAYEE)# с помощью функции set убираем дубликаты счетов получателя
DATEIN = set(DATEIN)# с помощью функции set убираем дубликаты дат

# print(tA_PAYER_PAYEE_DATEIN)
# print(tO_PAYER_PAYEE_DATEIN)

total_amount_PAYER = total_amount(loaded_dict_PAYER,PAYER) #общая сумма операций плательщика
total_operation_PAYER = total_operati(loaded_dict_PAYER,PAYER)# общие количество операций плательщика
max_amount_operation_PAYER = max_amount(loaded_dict_PAYER,PAYER)

total_amount_PAYEE = total_amount(loaded_dict_PAYEE,PAYEE)#общая сумма операций получателя
total_operation_PAYEE = total_operati(loaded_dict_PAYEE,PAYEE)#общая количество операций получателя
max_amount_operation_PAYEE = max_amount(loaded_dict_PAYEE,PAYEE)

total_amount_DATEIN = total_amount(loaded_dict_DATEIN,DATEIN)#общая сумма операций за каждую дату
total_operation_DATEIN = total_operati(loaded_dict_DATEIN,DATEIN)#общая количество операций за дату


# write_excel(tA_PAYER_PAYEE,'Total Amount Payer Payee')

write_excel(total_amount_PAYER,'a)Total Amount Payer')
write_excel(total_operation_PAYER,'c)Total Operation Payer')
write_excel(max_amount_operation_PAYER,'k)Max_amount Payer')

write_excel(total_amount_PAYEE,'b)Total Amount Payee')
write_excel(total_operation_PAYEE,'d)Total Operation Payee')
write_excel(max_amount_operation_PAYEE,'l)Max_amount Payee')

write_excel(total_amount_DATEIN,'i)Total amount DateIn')
write_excel(total_operation_DATEIN,'j)Total operation DateIn')


print('Всего плательщиков: '+str(len(PAYER))+'\n'+'Всего получателей: ' + str(len(PAYEE)))