unit_info = {
    "probo" : {
        "name" : "프로브",
        "mineral" : 50,
        "gas" : 0,
        "hp" : 20,
        "shield" : 20,
        "demage" : 5
    },
        "zealot" : {
        "name" : "질럿",
        "mineral" : 100,
        "gas" : 0,
        "hp" : 100,
        "shield" : 60,
        "demage" : 16
    },
        "dragon" : {
        "name" : "드라군",
        "mineral" : 125,
        "gas" : 50,
        "hp" : 100,
        "shield" : 80,
        "demage" : 20
    }
}
class unit:
    """
    속성 : 이름 , 체력, 방어막, 공격력
    """
    def __init__(self,name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage

#플레이어 클래스

class player:
    """
    속성 : 닉네임, 미네랄, 가스, 유닛리스트
    매서드 : 유닛생산 하기
    """

    def __init__(self,nickname, mineral, gas, unit_list =[]):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    def produce(self, name, mineral,gas,hp, shield, demage):
        if self.mineral - mineral <0:
            print('미네랄이 부족합니다.')
        elif self.gas - gas < 0:
            print('가스가 부족합니다.')
        else:
            self.mineral -= mineral
            self.gas -= gas
            Unit = unit(name, hp, shield, demage)
            self.unit_list.append(Unit)
            print(f'{name} 을(를) 생산합니다.')

#v플레이어 생성

player1 = player('bisu', 400, 50)

            

#유닛생성
player1.produce(unit_info['probo']['name'], unit_info['probo']['mineral'], unit_info['probo']['gas'],
                unit_info['probo']['hp'], unit_info['probo']['shield'],unit_info['probo']['demage'])
player1.produce(unit_info['zealot']['name'], unit_info['zealot']['mineral'], unit_info['zealot']['gas'],
                unit_info['zealot']['hp'], unit_info['zealot']['shield'],unit_info['zealot']['demage'])
player1.produce(unit_info['dragon']['name'], unit_info['dragon']['mineral'], unit_info['dragon']['gas'],
                unit_info['dragon']['hp'], unit_info['dragon']['shield'],unit_info['dragon']['demage'])                                


#생산된 모든 유닛 확인

for Unit in player1.unit_list:
    print(f'{Unit.name} 체력  : {Unit.hp}  방어막 : {Unit.shield} 공격력 : {Unit.demage} ')