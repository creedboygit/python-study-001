class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"나는 {self.name} {self.age}살")


shark = Monster("상어", 7)
shark.say()

wolf = Monster("늑대", 4)
wolf.say()
