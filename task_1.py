# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        pass


class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def display_info(self):
        print(f"Fish name: {self.name}")
        print(f"Water type: {self.water_type}")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def display_info(self):
        print(f"Bird name: {self.name}")
        print(f"Wingspan: {self.wingspan}")


class Insect(Animal):
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs

    def display_info(self):
        print(f"Insect name: {self.name}")
        print(f"Number of legs: {self.legs}")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Fish":
            return Fish(**kwargs)
        elif animal_type == "Bird":
            return Bird(**kwargs)
        elif animal_type == "Insect":
            return Insect(**kwargs)
        else:
            raise ValueError("Invalid animal type")


# Пример использования:

fish = AnimalFactory.create_animal("Fish", name="Nemo", water_type="Saltwater")
fish.display_info()

bird = AnimalFactory.create_animal("Bird", name="Eagle", wingspan=2.5)
bird.display_info()

insect = AnimalFactory.create_animal("Insect", name="Ant", legs=6)
insect.display_info()




