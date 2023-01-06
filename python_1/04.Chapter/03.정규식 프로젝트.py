#https://regexr.com/63cii

datas =['2022/08/08',
'1000/01/01',
'9999/12/31',
'900/02/02',
'12000/10/26',
'2021/13/01',
'2023/2/02',
'2024/06/3',
'2023/06/35',]
regs = '^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$'
import re

for data in datas:
    matchobj = re.match(regs, data)
    result = (lambda x : True if x != None else False)(matchobj)

    print(f'{data} ,{result}')

