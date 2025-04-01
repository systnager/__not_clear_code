class Hero:
    def __init__(self, name):
        self.name = name
        self.inventory = {
            "Armor": [],
            "Sword": [],
            "Staff": [],
            "Artifact": []
        }

    def add_item(self, category, item):
        if category in self.inventory:
            self.inventory[category].append(item)

    def show_inventory(self):
        inventory_str = []
        for category, items in self.inventory.items():
            if items:
                inventory_str.append(f"{category}: {', '.join(items)}")
        return f"{self.name} має інвентар: {', '.join(inventory_str)}"


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.class_type = "Warrior"


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.class_type = "Mage"


class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.class_type = "Paladin"


def Armor(hero, item="Basic Armor"):
    hero.add_item("Armor", item)
    return hero


def Sword(hero, item="Basic Sword"):
    hero.add_item("Sword", item)
    return hero


def Staff(hero, item="Magic Staff"):
    hero.add_item("Staff", item)
    return hero


def Artifact(hero, item="Common Artifact"):
    hero.add_item("Artifact", item)
    return hero


if __name__ == "__main__":
    warrior = Warrior("Arthur")
    mage = Mage("Gandalf")
    paladin = Paladin("Uther")

    warrior = Armor(Sword(warrior, "Excalibur"))
    mage = Armor(Staff(mage, "Staff of Wisdom"))
    paladin = Armor(Sword(Artifact(paladin, "Holy Grail"), "Divine Sword"))

    print(warrior.show_inventory())
    print(mage.show_inventory())
    print(paladin.show_inventory())
