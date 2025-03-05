class Subscription:
    def __init__(self, name, monthly_fee, min_period, channels, features):
        self.name = name
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels
        self.features = features

    def __str__(self):
        return f"Subscription: {self.name}\nMonthly Fee: ${self.monthly_fee}\nMin Period: {self.min_period} months\nChannels: {', '.join(self.channels)}\nFeatures: {', '.join(self.features)}"

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__("Domestic Subscription", 10, 1, ["Local News", "Sports", "Music"], ["HD Quality", "No Ads"])

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__("Educational Subscription", 15, 3, ["Educational Channels", "Documentaries"], ["HD Quality", "Exclusive Educational Content"])

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__("Premium Subscription", 25, 6, ["All Channels", "Premium Sports", "Music", "Movies"], ["4K Quality", "No Ads", "Exclusive Content", "Offline Mode"])

class WebSite:
    @staticmethod
    def buy_subscription(subscription_type):
        if subscription_type == "Domestic":
            return DomesticSubscription()
        elif subscription_type == "Educational":
            return EducationalSubscription()
        elif subscription_type == "Premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")

class MobileApp:
    @staticmethod
    def buy_subscription(subscription_type):
        if subscription_type == "Domestic":
            return DomesticSubscription()
        elif subscription_type == "Educational":
            return EducationalSubscription()
        elif subscription_type == "Premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")

class ManagerCall:
    @staticmethod
    def buy_subscription(subscription_type):
        if subscription_type == "Domestic":
            return DomesticSubscription()
        elif subscription_type == "Educational":
            return EducationalSubscription()
        elif subscription_type == "Premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")

def main():
    print("Buying subscription via WebSite:")
    website_subscription = WebSite.buy_subscription("Premium")
    print(website_subscription)

    print("\nBuying subscription via MobileApp:")
    mobile_subscription = MobileApp.buy_subscription("Educational")
    print(mobile_subscription)

    print("\nBuying subscription via ManagerCall:")
    manager_subscription = ManagerCall.buy_subscription("Domestic")
    print(manager_subscription)

if __name__ == "__main__":
    main()
