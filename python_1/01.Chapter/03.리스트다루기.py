#리스트 매서드

#리스트 데이터 삭제 
furits = ['apply', 'orange', 'mango']

del furits[1]
print(furits)
#리스트 정렬
number = [5,8,1,2,6,8,1]
number.sort()
print(number)

#enumerate
titles = ['출석','출석인증', '인증']

for index, title in enumerate(titles):
    print(f'{index} 번쨰 글입니다. {title}')
