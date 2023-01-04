#리스트 할당 방식

x = [1,2,3,4,5]
y = x.copy()
y[2] = 0
print(x)
print(y)
print(id(x))
print(id(y))

#리스트 복사 방식

a = [1,2,5,86,3,4]
b = a.copy()
b[2] = 0
print(a)
print(b)
print(id(a))
print(id(b))

#w중첩리스트 복사 방식
import copy

c= [[1,2], [3,4,5]]
d = copy.deepcopy(c)
d[0][0] = 0
print(c)
print(d)