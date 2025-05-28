class Product:
    def display(self):
        return "Generic product details"

class Electronics(Product):
    def display(self):  
        return "Electronics: Display specs like processor, RAM, etc."

class Clothing(Product):
    def display(self):  
        return "Clothing: Display size, color, and material"

laptop = Electronics()
shirt = Clothing()
print(laptop.display())  # Output: Electronics: Display specs like processor, RAM, etc.
print(shirt.display())   # Output: Clothing: Display size, color, and material


#MRO real life example
class Grandparent:
    def trait(self):
        return "I have wise life advice from years of experience."

class Parent1(Grandparent):
    def trait(self):
        return "I have a strong work ethic."

class Parent2(Grandparent):
    def trait(self):
        return "I have a great sense of humor."

class Child(Parent1, Parent2):
    def show_traits(self):
        return self.trait()


child = Child()

print(child.show_traits())  # Output: I have a strong work ethic.
print(Child.__mro__)  # Show the Method Resolution Order