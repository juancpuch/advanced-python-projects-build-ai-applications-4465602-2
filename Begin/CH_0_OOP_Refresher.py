# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition

# Constructor (Initialization) - __init__ method

# Encapsulation: Attributes (make and model) are encapsulated within the class.


# Method - start_engine

# Encapsulation: Accessing attributes through self.


# Creating instances (objects) of the Car class

# Inheritance: Car is a class that can be used to create objects (instances).
# Abstraction: We create objects without worrying about the internal details of the Car class.

# Creating the first car (object)

# Creating the second car (object)


# Accessing object attributes

# Encapsulation: Accessing object attributes (make and model) using dot notation.


# Calling object methods

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).


# Method Call - start_engine
class Car: 
  def __init__ (self, make, model):
    self.make = make
    self.model = model
  
  def start_engine(self):
    print(f"The {self.make} {self.model}'s engine is running!")

  
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

print(f"I have a {car1.make} {car1.model}.")
print(f"I aslo own a {car2.make} {car2.model}.")

car1.start_engine()
car2.start_engine()