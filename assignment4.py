# Method Overriding Example
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):  # Overrides the parent class method
        return "Woof!"

class Cat(Animal):
    def sound(self):  # Overrides the parent class method
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!


# Method Overloading Workaround Example
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))          # Output: 5 (a=5, b=0, c=0)
print(calc.add(5, 3))       # Output: 8 (a=5, b=3, c=0)
print(calc.add(5, 3, 2))    # Output: 10 (a=5, b=3, c=2)



#MRO example
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()  # Output: Class B #When d.show() is called, Python follows the MRO to find the method. The MRO is [D, B, C, A, object], so B's show method is used.
print(D.__mro__)  