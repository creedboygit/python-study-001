class Item:
    def __init__(self, name, price, weight, is_droppable):
        self.name = name
        self.price = price
        self.weight = weight
        self.is_droppable = is_droppable

    def sale(self):
        print(f"[{self.name}] 판매 가격은 [{self.price}]")

    def discard(self):
        if self.is_droppable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")


class WearableItem(Item):
    def __init__(self, name, price, weight, is_droppable, effect):
        super().__init__(name, price, weight, is_droppable)
        self.effect = effect

    def wear(self):
        print(f"[{self.name}] 착용했습니다. {self.effect}")


class UsableItem(Item):
    def __init__(self, name, price, weight, is_droppable, effect):
        super().__init__(name, price, weight, is_droppable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}] 사용했습니다. {self.effect}")


sword = WearableItem("닌자검", 30000, 3.5, True, "체력 5000 증가, 마력 5000 증가")
sword.wear()
sword.sale()
sword.discard()

potion = UsableItem("포션", 145000, 0.1, False, "투명효과 300초 지속")
potion.discard()
potion.sale()
potion.use()




