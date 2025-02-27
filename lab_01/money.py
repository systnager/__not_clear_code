class Money:
    def __init__(self):
        self.whole_amount = 0
        self.part_amount = 0

    def add_funds(self, whole_amount=0, part_amount=0):
        total_part = self.part_amount + part_amount
        total_whole = self.whole_amount + whole_amount + total_part // 100
        self.whole_amount = total_whole
        self.part_amount = total_part % 100

    def minus_funds(self, whole_amount=0, part_amount=0):
        self.add_funds(whole_amount * -1, part_amount * -1)

    def get_whole_amount(self):
        return self.whole_amount

    def get_part_amount(self):
        return self.part_amount

    def set_funds(self, whole_amount, part_amount):
        total_whole = whole_amount + part_amount // 100
        total_part = part_amount % 100
        self.whole_amount = total_whole
        self.part_amount = total_part

    def total_cents(self):
        return self.whole_amount * 100 + self.part_amount

    def __str__(self):
        return f"{self.whole_amount}.{self.part_amount:02d}"
