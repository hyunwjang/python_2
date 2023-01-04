#문자열 포매딩이 없다면?
#기준님 수강기간이 7일 남았습니다.

name = '기준'
duration = 7

messsage = name + "님 수강기간이 " +str(duration) + '일 남았습니다.'

print(messsage)

 #문자열 포매딩 사용시
messsage_format = f'{name}님 수강기간이 {duration} 일 남았습니다.'
print(messsage_format)

#format 매서드
a = 'hello {1} {2} {0}'.format('apply', 'pineapply', 'pen')
print(a)

a = 'hello {} {} {}'.format('apply', 'pineapply', 'pen')
print(a)

#f-string 사용

name1 = 'apply'
name2 = 'pineapply'
name3 = 'pen'

c = f'hello {name1} {name2} {name3}'
print(c)