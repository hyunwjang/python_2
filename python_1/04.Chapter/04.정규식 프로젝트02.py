#1.이메일 ID파트와 host 파트가 있다 ( ID@host)
#2.ID파트는  영문 대소문자, 숫자 특수문자 (-_)가 들어갈수 있다
#3host 파트는  영문, 대소문자, 숫자, 특수문자(-)
#4host 파트는 2개 이상의 도메인으로 구성 될 수 있다

import re


datas =[
    'startcoding@maver.com'
,'start-coding@maver.com'
,'start_coding@maver.co.kr'
,'startcoding@k-mail.com'
,'@maver.com'
,'startcoding?@k-mail.com'
,'startcoding@k-mail'
,'startcoding@maver']

reg = re.compile('^[\w-]+@[a-zA-Z0-9-]+.\.[a-zA-Z0-9-.]+$')

for idx, data in enumerate(datas):
    matchobj = reg.match(data)
    result = (lambda x : True if x != None else False)(matchobj)
    print(f'{idx}.{data} : {result}')
