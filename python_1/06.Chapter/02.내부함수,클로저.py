#내부함수
# 함수안에 또다른 함수를 정의할수 있다


def outer(name):
    def inner(): #클로저 함수
        print(name, "님 안녕하세요 ")
    return inner

func = outer('startconding')

func()



#2.클로저 함수
#함수가 종료되어도 자원을 사용할 수 있다.

# * 클로저가 될 조건
#내부 함수이여야한다
#외부함수의 변수를 참조해야한다
#외부함수가 내부 함수를 반환하여야 한다

def greeting(name, age, gender):
    def inner():
        print(name , "님 안녕하세요 ")
        print(age , "세입니다." )
        print(gender , "입니다. ")
    return inner

closure = greeting('나미', 28,'female')
closure()
print(dir(closure))
print('*'*20)
print(type(closure.__closure__))
print('*'*20)
print(dir(closure.__closure__))
print(closure.__closure__)
print('*'*20)
print(dir(closure.__closure__[0]))

print(closure.__closure__[0].cell_contents)
print(closure.__closure__[1].cell_contents)
print(closure.__closure__[2].cell_contents)

