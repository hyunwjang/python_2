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
    def __init__(self,name, hp, shield, demage):#객체를 생성할때 출력
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        unit.count +=1
        print(f'[{self.name}] (이)가 생성되었습니다.')
  
    def __str__(self):#객체를 출력할때 출력
        return f'[{self.name}] 체력 : {self.hp}, 방어막 : {self.shield}, 공격력 : {self.demage}'

    #인슨터스 매서드(instance method)

    def hit(self, demage):
        #방어막 변경
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield  = 0

        #체력변경

        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0
        
    #클래스 매서드 (class method)
    # 클래스 속성에 접근하는 매서드
    @classmethod
    def print_count(cls):
        print(f'생성된 유닛 개수 : [{cls.count}]개')


probo = unit('프로브', 20,20,5)        
zealot = unit('질럿', 100, 60 , 16)
dragoon = unit('질럿', 100, 80 , 20)

probo.hit(16)
print(probo)

probo.hit(16)
print(probo)

probo.hit(16)
print(probo)

unit.print_count()

print(dir(probo))