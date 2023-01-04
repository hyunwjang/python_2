import re

# 1) re 매서드 

str = 'love people arond you ,  you love your work, love your self'

#1) match 문자열의 처음부터 검색 (결과 1개의 match 객체)

reslut = re.match('love',str)
print(reslut)

#2) search : 문자열의 전체를 검색 ( 결과 1개의 match객체)

result = re.search('people', str)
print(result)

#3) findall : 문자열의 전체를 검색 ( 결과 : 문자열 리스트)

result = re.findall('love', str)
print(result)

#4) finditer : 문자열의 전체를 검색( 결과 : match 객체 이터레이터)
results = re.finditer('love', str)
print(results)

for result in results:
    print(reslut)

#5) fullmatch 패턴과 문자열이 완벽하게 일치하는지 검사
str2 = 'Hey guys, read books'
result = re.fullmatch('.*',str2)
print(result)

#2. match object의 매서트
result = re.search('people', str)


#1) group : 매칭된 문자열을 반환
print(result.group())

#2) start(): 매칭된 문자열의 시작 위치 반환
print(result.start())

#2) end() :매칭된 문자열의 끝위치 반환
print(result.end())

#3) span() : 매칭된 문자열의 (시작, 끝) 위치를 반환
print(result.span())