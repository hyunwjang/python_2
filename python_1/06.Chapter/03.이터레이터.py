# 순서가 있는 자료형
#문자열 리스트, 튜플 딕셔너리 , range객체

#이터레이터 클래스를 정의 해준다 

#__iter__를 정의해준다
#____를 정의해준다
for i in "123":
    print(i)

for i in [10,20,30]:
    print(i)


print(dir([10,20,30]))
print(type([10,20,30].__iter__))

iter_obj = [10,20,30].__iter__()


print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())