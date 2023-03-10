import re

#전화번호 정규표현식 연습
#http://regexr.com/63bls

#1.group 

#1) 매칭되는 문자열 한개
str1 = '010-2343-3333'
result = re.match('\d{2,3}-\d{3,4}-(\d{4})$', str1)

print(result)
print(result.group())
print(result.group(1))

#2)매칭되는 문자열이 여러개

str2 = '010-2343-7888,010-2343-1234,010-2343-5678,010-2343-9999,010-2343-2222'
results = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=|$)',str2)
for idx, result in enumerate(results):
    print(f'{idx},{result.group(1)}')

#2. substitution(교체)
str3 = '010-2343-3333'
result = re.sub('(?<=\d{3}-\d{4}-)\d{4}','****', str3)
#전방탐색 범위 유동 가능
#후방탐색 범위 고정
print(result)
