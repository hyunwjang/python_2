class unit:
    """
    인스턴스속성 : 이름 체력, 방어막, 공격력
    -> 객체마다 다른값을 가지는 속성

    클래스 속성 : 전체 유닛 개수
    ->모든 객체가 공유하는 속성 (count)

    비공개 속성
    -> 클래스 안에서만 사용 가능한 속성
    """

    count = 0
    def __init__(self,name, hp, shield, demage):
        self.name = name
        self.__hp = hp
        self.shield = shield
        self.demage = demage
        unit.count +=1
        print(f'[{self.name}] (이)가 생성되었습니다.')
  
    def __str__(self):
        return f'[{self.name}] 체력 : {self.__hp}, 방어막 : {self.shield}, 공격력 : {self.demage}'


probo = unit('프로브', 20,20,5)        
zealot = unit('질럿', 100, 60 , 16)
dragoon = unit('질럿', 100, 80 , 20)

#인스턴스 수정
# probo.demage +=1
# print(probo.demage)

# #비공개 송성 접근
# probo.__hp = 8888
# print(probo)
# #네임랭글리(name_mangling)
# probo._unit__hp = 8999
# print(probo)

# #클래스 속성 전체유닛 개수
# print(unit.count)
