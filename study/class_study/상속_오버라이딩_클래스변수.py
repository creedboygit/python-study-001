class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"[{self.name}] : 지상으로 이동")


# 자식 클래스
class Wolf(Monster):
    pass


class Shark(Monster):
    def move(self):
        print(f"[{self.name}] : 헤엄치기")


class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] : 날기")


wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("샤크", 3000, 400)
shark.move()

dragon = Dragon("드래곤", 8000, 300)
dragon.move()
