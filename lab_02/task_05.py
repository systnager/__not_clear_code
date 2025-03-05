class HeroBuilder:
    def __init__(self, name):
        self.hero = {
            "name": name,
            "height": None,
            "build": None,
            "hair_color": None,
            "eye_color": None,
            "clothing": None,
            "inventory": [],
            "good_deeds": [],
            "actions": []
        }

    def set_height(self, height):
        self.hero["height"] = height
        return self

    def set_build(self, build):
        self.hero["build"] = build
        return self

    def set_hair_color(self, color):
        self.hero["hair_color"] = color
        return self

    def set_eye_color(self, color):
        self.hero["eye_color"] = color
        return self

    def set_clothing(self, clothing):
        self.hero["clothing"] = clothing
        return self

    def add_inventory(self, item):
        self.hero["inventory"].append(item)
        return self

    def add_good_deed(self, deed):
        self.hero["good_deeds"].append(deed)
        return self

    def add_action(self, action):
        self.hero["actions"].append(action)
        return self

    def build(self):
        return self.hero


class EnemyBuilder:
    def __init__(self, name):
        self.enemy = {
            "name": name,
            "height": None,
            "build": None,
            "hair_color": None,
            "eye_color": None,
            "clothing": None,
            "inventory": [],
            "evil_deeds": [],
            "actions": []
        }

    def set_height(self, height):
        self.enemy["height"] = height
        return self

    def set_build(self, build):
        self.enemy["build"] = build
        return self

    def set_hair_color(self, color):
        self.enemy["hair_color"] = color
        return self

    def set_eye_color(self, color):
        self.enemy["eye_color"] = color
        return self

    def set_clothing(self, clothing):
        self.enemy["clothing"] = clothing
        return self

    def add_inventory(self, item):
        self.enemy["inventory"].append(item)
        return self

    def add_evil_deed(self, deed):
        self.enemy["evil_deeds"].append(deed)
        return self

    def add_action(self, action):
        self.enemy["actions"].append(action)
        return self

    def build(self):
        return self.enemy


class CharacterDirector:
    def __init__(self, hero_builder, enemy_builder):
        self.hero_builder = hero_builder
        self.enemy_builder = enemy_builder

    def construct(self):
        hero = (self.hero_builder
                .set_height("6'0\"")
                .set_build("Athletic")
                .set_hair_color("Brown")
                .set_eye_color("Blue")
                .set_clothing("Suit")
                .add_inventory("Diplomatic Skills")
                .add_good_deed("Led the Allies to victory in WWII")
                .add_action("LandLease")
                .add_action("Call Parliament")
                .add_action("Negotiate with Allies")
                .build())

        enemy = (self.enemy_builder
                 .set_height("5'8\"")
                 .set_build("Stocky")
                 .set_hair_color("Blonde")
                 .set_eye_color("Blue")
                 .set_clothing("Nazi Uniform")
                 .add_inventory("Nazi Propaganda")
                 .add_evil_deed("Started WWII")
                 .add_evil_deed("Genocide of Jews")
                 .add_action("Holocaust")
                 .add_action("Invade countries")
                 .add_action("Demand Capitulation")
                 .build())

        return hero, enemy


def main():
    hero_builder = HeroBuilder("Franklin D. Roosevelt")
    enemy_builder = EnemyBuilder("Adolf Hitler")

    director = CharacterDirector(hero_builder, enemy_builder)
    hero, enemy = director.construct()

    print("Hero:")
    for key, value in hero.items():
        print(f"{key}: {value}")

    print("\nEnemy:")
    for key, value in enemy.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
