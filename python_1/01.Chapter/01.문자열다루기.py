# 2. find
# 문자열 찾기
b = ' hello world'.find('world7')
print(b)

#3. split
#문자열 분리
v ='나이키 245 k1231 600999'
print(v.split())

v ='나이키: 245:k1231 :600999'
print(v.split(':'))

#4. strip
#문자열 공백제거
c = '             year         '
print(c.lstrip())
print(c.rstrip())
print(c.strip())