#이터레이터 만드는 함수

#함수안에yield를 사용한데 (return과 비교)
#제너레이터 표현식을 사용할 수 있다 .
#메모리 효율이 좋다 

def season_generator(*args):
    for arg in args:
        yield arg#리턴 지연

g = season_generator('spring', 'summer', 'autumn', 'winter')

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

def func():
    print('첫번쨰 작업중')
    yield 1
    
    print('두번쨰 작업중')
    yield 2
    
    print('세번쨰 작업중')
    yield 3

ga = func()
data = ga.__next__()
print(data)

data = ga.__next__()
print(data)

data = ga.__next__()
print(data)
