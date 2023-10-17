# 7
class Animal:
   def voice(self):
       pass

   counter = 0

   def __init__(self):
       Animal.counter += 1

   @staticmethod
   def countChildren():
       print(Animal.counter)


class Dog(Animal):
    def voice(self):
        print("I am funny dog")


class Parrot(Animal):
    def voice(self):
        print("I am loud parrot")


class Cat(Animal):
    def voice(self):
        print("I am beautiful cat")


cat = Cat()
cat.voice()

dog = Dog()
dog.voice()

parrot = Parrot()
parrot.voice()

Animal.countChildren()
