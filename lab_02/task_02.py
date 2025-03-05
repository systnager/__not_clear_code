from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand, model, specifications):
        self.brand = brand
        self.model = model
        self.specifications = specifications

    @abstractmethod
    def create_device(self):
        pass

    def __str__(self):
        return f"{self.brand} {self.model}\nSpecifications: {', '.join(self.specifications)}"


class Laptop(Device):
    def create_device(self):
        return f"Laptop {self.model} created by {self.brand}"


class Netbook(Device):
    def create_device(self):
        return f"Netbook {self.model} created by {self.brand}"


class Tablet(Device):
    def create_device(self):
        return f"Tablet {self.model} created by {self.brand}"


class Smartphone(Device):
    def create_device(self):
        return f"Smartphone {self.model} created by {self.brand}"


class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self, model, specifications):
        pass

    @abstractmethod
    def create_netbook(self, model, specifications):
        pass

    @abstractmethod
    def create_tablet(self, model, specifications):
        pass

    @abstractmethod
    def create_smartphone(self, model, specifications):
        pass


class IProneFactory(DeviceFactory):
    def create_laptop(self, model, specifications):
        return Laptop("IProne", model, specifications)

    def create_netbook(self, model, specifications):
        return Netbook("IProne", model, specifications)

    def create_tablet(self, model, specifications):
        return Tablet("IProne", model, specifications)

    def create_smartphone(self, model, specifications):
        return Smartphone("IProne", model, specifications)


class KiaomiFactory(DeviceFactory):
    def create_laptop(self, model, specifications):
        return Laptop("Kiaomi", model, specifications)

    def create_netbook(self, model, specifications):
        return Netbook("Kiaomi", model, specifications)

    def create_tablet(self, model, specifications):
        return Tablet("Kiaomi", model, specifications)

    def create_smartphone(self, model, specifications):
        return Smartphone("Kiaomi", model, specifications)


class BalaxyFactory(DeviceFactory):
    def create_laptop(self, model, specifications):
        return Laptop("Balaxy", model, specifications)

    def create_netbook(self, model, specifications):
        return Netbook("Balaxy", model, specifications)

    def create_tablet(self, model, specifications):
        return Tablet("Balaxy", model, specifications)

    def create_smartphone(self, model, specifications):
        return Smartphone("Balaxy", model, specifications)


class DeviceFactoryManager:
    def __init__(self):
        self.brands = {
            "IProne": IProneFactory(),
            "Kiaomi": KiaomiFactory(),
            "Balaxy": BalaxyFactory()
        }

    def create_device(self, brand, device_type, model, specifications):
        if brand not in self.brands:
            raise ValueError("Unknown brand")
        brand_instance = self.brands[brand]

        if device_type == "Laptop":
            return brand_instance.create_laptop(model, specifications)
        elif device_type == "Netbook":
            return brand_instance.create_netbook(model, specifications)
        elif device_type == "Tablet":
            return brand_instance.create_tablet(model, specifications)
        elif device_type == "Smartphone":
            return brand_instance.create_smartphone(model, specifications)
        else:
            raise ValueError("Unknown device type")


def main():
    factory_manager = DeviceFactoryManager()

    print("Creating IProne Laptop:")
    iprone_laptop = factory_manager.create_device("IProne", "Laptop", "XPro 15", ["16GB RAM", "512GB SSD", "Intel i7"])
    print(iprone_laptop)

    print("\nCreating Kiaomi Smartphone:")
    kiaomi_smartphone = factory_manager.create_device("Kiaomi", "Smartphone", "KX3", ["6GB RAM", "128GB Storage", "5G Support"])
    print(kiaomi_smartphone)

    print("\nCreating Balaxy Tablet:")
    balaxy_tablet = factory_manager.create_device("Balaxy", "Tablet", "TabX", ["4GB RAM", "64GB Storage", "10.5\" Screen"])
    print(balaxy_tablet)


if __name__ == "__main__":
    main()
