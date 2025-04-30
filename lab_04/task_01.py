class SupportHandler:
    def __init__(self, name, questions, triggers):
        self.name = name
        self.questions = questions
        self.triggers = triggers
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return self.next

    def handle(self):
        for question in self.questions:
            answer = input(question).strip().lower()
            if answer in self.triggers:
                print(f"Ваша проблема передана до {self.name}. Очікуйте на допомогу.")
                return True
        if self.next:
            return self.next.handle()
        return False


def build_chain():
    h1 = SupportHandler(
        "Рівень 1: Загальні питання",
        [
            "Чи є у вас технічна проблема з Інтернетом? (так/ні): ",
            "Чи хочете ви дізнатися про додаткові послуги? (так/ні): ",
            "Чи маєте ви питання щодо рахунку або оплати? (так/ні): "
        ],
        ["так", "т", "yes", "y"]
    )

    h2 = SupportHandler(
        "Рівень 2: Проблеми з оплатою Інтернету",
        [
            "Чи маєте ви проблему з оплатою Інтернету? (так/ні): ",
            "Чи виникли проблеми при сплаті за Інтернет? (так/ні): "
        ],
        ["так", "т", "yes", "y"]
    )

    h3 = SupportHandler(
        "Рівень 3: Проблеми з використанням Інтернету",
        [
            "Чи є у вас проблема з підключенням до Інтернету? (так/ні): ",
            "Чи не працює Інтернет на вашому пристрої? (так/ні): "
        ],
        ["так", "т", "yes", "y"]
    )

    h4 = SupportHandler(
        "Рівень 4: Проблеми з входом до особистого акаунту",
        [
            "Чи не можете ви увійти до свого акаунту на сайті провайдера? (так/ні): ",
            "Чи забули ви пароль для входу в особистий акаунт? (так/ні): "
        ],
        ["так", "т", "yes", "y"]
    )

    h5 = SupportHandler(
        "Рівень 5: Питання про зміну тарифу",
        [
            "Чи хочете ви змінити тариф на більш дешевий? (так/ні): ",
            "Чи хочете ви змінити тариф на швидший Інтернет? (так/ні): "
        ],
        ["так", "т", "yes", "y"]
    )

    h6 = SupportHandler(
        "Рівень 6: Питання щодо додаткових послуг",
        [
            "Чи хочете ви підключити білий IP? (так/ні): ",
            "Чи хочете ви підключити IPTV? (так/ні): "
        ],
        ["так", "т", "yes", "y"]
    )

    h1.set_next(h2).set_next(h3).set_next(h4).set_next(h5).set_next(h6)
    return h1


def support_system():
    root = build_chain()
    while True:
        if root.handle():
            break
        print("Не вдалося визначити вашу проблему. Перезапуск меню...\n")


if __name__ == "__main__":
    support_system()
