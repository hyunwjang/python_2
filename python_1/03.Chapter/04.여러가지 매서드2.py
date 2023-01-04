class Math:

    #정적 매서드(static Method)
    #인스턴스를 만들필요가 없는 매서드

    @staticmethod
    def add(x, y):
        return x+y
    @staticmethod
    def sub(x, y):
        return x-y


print(Math.add(1,2))
print(Math.sub(5,2))