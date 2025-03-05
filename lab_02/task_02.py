class Device:
    def __init__(self, brand, model, specifications):
        self.brand = brand
        self.model = model
        self.specifications = specifications

    def __str__(self):
        return f"{self.brand} {self.model}\nSpecifications: {', '.join(self.specifications)}"


class Laptop(Device):
    def __init__(self, brand, model, specifications):
        super().__init__(brand, model, specifications)


class Netbook(Device):
    def __init__(self, brand, model, specifications):
        super().__init__(brand, model, specifications)


class EBook(Device):
    def __init__(self, brand, model, specifications):
        super().__init__(brand, model, specifications)


class Smartphone(Device):
    def __init__(self, brand, model, specifications):
        super().__init__(brand, model, specifications)


class IProne:
    def create_device(self, device_type, model, specifications):
        if device_type == "Laptop":
            return Laptop("IProne", model, specifications)
        elif device_type == "Netbook":
            return Netbook("IProne", model, specifications)
        elif device_type == "EBook":
            return EBook("IProne", model, specifications)
        elif device_type == "Smartphone":
            return Smartphone("IProne", model, specifications)
        else:
            raise ValueError("Unknown device type")


class Kiaomi:
    def create_device(self, device_type, model, specifications):
        if device_type == "Laptop":
            return Laptop("Kiaomi", model, specifications)
        elif device_type == "Netbook":
            return Netbook("Kiaomi", model, specifications)
        elif device_type == "EBook":
            return EBook("Kiaomi", model, specifications)
        elif device_type == "Smartphone":
            return Smartphone("Kiaomi", model, specifications)
        else:
            raise ValueError("Unknown device type")


class Balaxy:
    def create_device(self, device_type, model, specifications):
        if device_type == "Laptop":
            return Laptop("Balaxy", model, specifications)
        elif device_type == "Netbook":
            return Netbook("Balaxy", model, specifications)
        elif device_type == "EBook":
            return EBook("Balaxy", model, specifications)
        elif device_type == "Smartphone":
            return Smartphone("Balaxy", model, specifications)
        else:
            raise ValueError("Unknown device type")


class DeviceFactory:
    def __init__(self):
        self.brands = {
            "IProne": IProne(),
            "Kiaomi": Kiaomi(),
            "Balaxy": Balaxy()
        }

    def create_device(self, brand, device_type, model, specifications):
        if brand not in self.brands:
            raise ValueError("Unknown brand")
        brand_instance = self.brands[brand]
        return brand_instance.create_device(device_type, model, specifications)


def main():
    factory = DeviceFactory()

    print("Creating IProne Laptop:")
    iprone_laptop = factory.create_device("IProne", "Laptop", "XPro 15", ["16GB RAM", "512GB SSD", "Intel i7"])
    print(iprone_laptop)

    print("\nCreating Kiaomi Smartphone:")
    kiaomi_smartphone = factory.create_device("Kiaomi", "Smartphone", "KX3", ["6GB RAM", "128GB Storage", "5G Support"])
    print(kiaomi_smartphone)

    print("\nCreating Balaxy Netbook:")
    balaxy_netbook = factory.create_device("Balaxy", "Netbook", "Breeze 11", ["4GB RAM", "64GB Storage", "Intel Atom"])
    print(balaxy_netbook)


if __name__ == "__main__":
    main()
