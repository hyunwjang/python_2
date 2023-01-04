#1. map함수
#-사용이유
# 기존 리스트를 수정해서 새로운 리스트를 만들때 


#-사용 방법
# map(함수, 순서가 있는 자료형)
print(list(map(int, ['3','4','5','4'])))

# - 예제
# 리스트 모든 요소의 공백 제거
items = ['     로지텍 마우스  ', '앱솔키보드 ']

#1)for 문 사용
for i in range(len(items)):
    items[i] = items[i].strip()

print(items)

#2)map 사용
def strip_all(x):
    return x.strip()

items = list(map(strip_all, items))
print(items)
#3) 람다 함수 사용

itmes = list(map(lambda x : x.strip(), items))
print(itmes)

#2. 필터 함수
#-사용이유
#기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때 

#- 사용 방법
#fiter (함수, 순서가 있는 자료형)
def func(x):
    return x> 3

print(list(filter(func, [1,2,3,4,5,6,])))


#예제
#리스트에서 길이가 3이한인 문제들만 필터링
animals = ['cat', 'tiger', 'dog', 'bird', 'monkey']

# 1) for 문사용
result = []
for i in animals:
    if len(i) <=3:
        result.append(i)
print(result)

#3) fiter 사용
def word_check(x):
    return len(x) <= 3

result = list(filter(word_check , animals))
print(result)
#4) filter lambda 사용
result = list(filter(lambda x : len(x)<=3 ,animals))
print(result)
