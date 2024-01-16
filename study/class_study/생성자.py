class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health


goblin = Monster(300, 200, 400)
goblin.decrease_health(100)
print(goblin.get_health())

wolf = Monster(1300, 1200, 1100)
wolf.decrease_health(200)
print(wolf.get_health())


