# #실습문제 2.6.1
# #시간을 분으로
# #예제
# a = '1시간 30분'
# b = '2시간'
# c = '30분'

# time = input("시간을 입력해 주세요>>\n")
# t = time.split()
# min = 0
# hour = 0


# for ti in t:
#     if ti.find('분') >=0:
#         min  =int(ti.replace('분',''))
        
#     elif ti.find('시간') >=0:
#         hour  = int(ti.replace('시간',''))
#         hour =hour*60

# print(min +hour)


#++++++++++++++++++++++++++++++++++++sadf

time = input('시간을 입력해주세요 ')

if time.find('시간') ==-1:
    result = int(time.split('분')[0])
else:
    if time.find('분') ==-1:
        result = int(time.split('시간')[0])*60
    else:
        sub = time.split('시간')
        hour = int(sub[0])*60
        min = int(sub[1].split('분')[0])
        result = hour + min

print(result)