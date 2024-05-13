import pickle

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic sound"

    def eat(self):
        return f"{self.name} is eating."

# Наследование классов для разных типов животных
class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says tweet!"

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} says woof!"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} says hiss!"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Класс зоопарка с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, Age: {animal.age}")

    def list_staff(self):
        for person in self.staff:
            print(f"{person.name}, Position: {person.position}")

# Классы для сотрудников
class StaffMember:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(StaffMember):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")

class Veterinarian(StaffMember):
    def heal_animal(self, animal):
        print(f"{self.name} is treating {animal.name}")

# Функции для сохранения и загрузки зоопарка
def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)

def load_zoo(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Пример использования
zoo = Zoo()
zoo.add_animal(Bird("Parrot", 5))
zoo.add_staff(ZooKeeper("Alice", "Zookeeper"))
save_zoo(zoo, 'zoo.pickle')

loaded_zoo = load_zoo('zoo.pickle')
loaded_zoo.list_animals()
loaded_zoo.list_staff()

# Полиморфизм в действии
animals = [Bird("Parrot", 5), Mammal("Dog", 3), Reptile("Snake", 2)]
animal_sound(animals)