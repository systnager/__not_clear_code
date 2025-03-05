import copy

class Virus:
    def __init__(self, name, species, weight, age, children=None):
        self.name = name
        self.species = species
        self.weight = weight
        self.age = age
        self.children = children if children is not None else []

    def add_child(self, child_virus):
        self.children.append(child_virus)

    def __str__(self):
        return f"Virus: {self.name}, Species: {self.species}, Weight: {self.weight}kg, Age: {self.age} years"

    def clone(self):
        return copy.deepcopy(self)

def main():
    virus_father = Virus(name="ViralFather", species="VirusA", weight=0.1, age=5)
    virus_child_1 = Virus(name="ViralChild1", species="VirusA", weight=0.05, age=2)
    virus_child_2 = Virus(name="ViralChild2", species="VirusA", weight=0.06, age=1)

    virus_father.add_child(virus_child_1)
    virus_father.add_child(virus_child_2)

    virus_grandchild_1 = Virus(name="ViralGrandChild1", species="VirusA", weight=0.02, age=0.5)
    virus_grandchild_2 = Virus(name="ViralGrandChild2", species="VirusA", weight=0.03, age=0.3)

    virus_child_1.add_child(virus_grandchild_1)
    virus_child_2.add_child(virus_grandchild_2)

    print("Original Father Virus and its Children:")
    print(virus_father)
    for child in virus_father.children:
        print(child)
        for grandchild in child.children:
            print(grandchild)

    virus_father_clone = virus_father.clone()

    print("\nCloned Father Virus and its Children:")
    print(virus_father_clone)
    for child in virus_father_clone.children:
        print(child)
        for grandchild in child.children:
            print(grandchild)

if __name__ == "__main__":
    main()
