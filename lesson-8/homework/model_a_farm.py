class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', Age: {self.age}, Weight: {self.weight}kg)"


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says Moo!")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")


class Chicken(Animal):
    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def lay_egg(self):
        print(f"{self.name} laid an egg.")


class Sheep(Animal):
    def make_sound(self):
        print(f"{self.name} says Baaaaaaaaaa!")

    def rolling(self):
        print(f"{self.name} is rolling.")


def main():
    bessie = Cow("Mr.Mowee", 5, 500)
    clucky = Chicken("Chiken_Jokey", 2, 2)
    sheepy = Sheep("Qoravoy", 3, 120)

    farm = [bessie, clucky, sheepy]

    for animal in farm:
        print(animal)
        animal.eat()
        animal.sleep()
        animal.make_sound()
        if isinstance(animal, Cow):
            animal.produce_milk()
        elif isinstance(animal, Chicken):
            animal.lay_egg()
        elif isinstance(animal, Sheep):
            animal.rolling()
        print("------------------------------")


if __name__ == "__main__":
    main()
