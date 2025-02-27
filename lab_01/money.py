class Money:
    def __init__(self):
        self.whole_amount = 0
        self.part_amount = 0

    def add_funds(self, whole_amount=0, part_amount=0):
        self.part_amount += part_amount
        self.whole_amount += whole_amount + self.part_amount // 100
        self.part_amount = self.part_amount % 100

    def minus_funds(self, whole_amount=0, part_amount=0):
        self.add_funds(whole_amount * -1, part_amount * -1)

    def get_whole_amount(self):
        return self.whole_amount

    def get_part_amount(self):
        return self.part_amount
