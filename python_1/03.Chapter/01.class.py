class unit:
    """
    속성 : 이름 체력, 방어막, 공격력
    """

    #생성자(constructor)
    #객체를 생성할 떄 호출되는 매서드

    def __init__(self,name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        print(f'[{self.name}] (이)가 생성되었습니다.')
    #객체를 출력할 떄 호출되는 매서드
    def __str__(self):
        return f'[{self.name}] 체력 : {self.hp}, 방어막 : {self.shield}, 공격력 : {self.demage}'

#프로브 객체를 생성
probo = unit('프로브', 20,20,5)        


#질럿 객체를 생성
zealot = unit('질럿', 100, 60 , 16)

#드라군 객체를 생성
dragoon = unit('질럿', 100, 80 , 20)
print(probo)
print(zealot)
print(dragoon)
print(probo.name)