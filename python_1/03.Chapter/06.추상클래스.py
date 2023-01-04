from abc import *

class item(metaclass = ABCMeta):
    """
    속성 : 이름
    매서드 : 줍기, 버리기
    """
    def __init__(self, name):
        self.name = name
    
    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f'[{self.name}]을(를) 버렸습니다.')
    @abstractmethod
    def use(self):
        pass

class weapon(item):
    """
    속성 : 공격력
    매서드 : 공격하기
    """
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage
    def use(self):
        print(f'[{self.name}]을(를) 이용해 {self.demage}로 공격 받았습니다.')

    
class healingitem(item):
    """
    속성 : 회복량
    매서드 : 사용하기
    """
    def __init__(self, name, recovery_amout):
        super().__init__(name)
        self.recovery_amout = recovery_amout
    
    def use(self):
        print(f'[{self.name}]을(를) 사용합니다. {self.recovery_amout} 회복')

m16  = weapon('m16', 110)
bungdae = healingitem('붕대', 20)

m16.use()
bungdae.use()
