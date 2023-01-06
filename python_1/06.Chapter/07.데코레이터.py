#데토레이터
#함수의 앞 , 뒤로 부과적인 기능을 넣어주고 싶을때 사용

#로깅 , 권한확인

def logger(func):
    def wrapper(arg):
        print('함수시작')
        func(arg)#함수실행
        print('함수끝')
    return wrapper

@logger
def print_hello(name):
 
    print('hello startcoding',name)
   


@logger
def print_bye(name):
  
    print('bye fastcampus',name)


print_hello('start conding')
print_bye('fast cam')
    