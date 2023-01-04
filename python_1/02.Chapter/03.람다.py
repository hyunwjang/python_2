#기존함수
def minus_one(a):
    return a-1

#람다함수
lambda a: a-1

#람다 함수 호출 방법 1. 함수 자체를 호출
print((lambda a : a-1)(10))

#람다 함수 호출 방법 2. 변수에 담아서 호출
minus_one2 = lambda a : a-1
print(minus_one2(200))

#람다 함수에  if문 사용

#기존함수
def is_postitive_number(a):
    if a> 0:
        return True
    else:
        return False
#람다함수
lambda a : True if a>0 else False
#람다함수 호출
print((lambda a : True if a>0 else False)(-2))
is_postitive =(lambda a : True if a>0 else False)
print(is_postitive(2))