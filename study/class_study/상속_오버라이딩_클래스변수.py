import random


class Monster:

    max_num = 1000

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f"[{self.name}] : 지상으로 이동")


# 자식 클래스
class Wolf(Monster):
    pass


class Shark(Monster):
    def move(self):
        print(f"[{self.name}] : 헤엄치기")


class Dragon(Monster):

    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):
        print(f"[{self.name}] : 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0, 2)]}")


wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 8000, 300)
dragon.move()
dragon.skill()
print(dragon.max_num)
