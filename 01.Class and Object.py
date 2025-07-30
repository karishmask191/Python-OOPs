'''
# Here's a fresh, easy-to-understand explanation of all major Python OOP concepts, each with a simple real-life example and clean code.
1.Class & Object:
A class is a blueprint, and an object is a real-world instance of that blueprint.

=> Example: Dog Tracker (Think of a class like a dog registration form.It has fields like name and breed.Each dog you register is an object — it's like filling that form with real details.)
   So:    
      Class = Form (blueprint)
      Object = Filled form (real dog)
   
=> Example Code:
--------------------
# Define the class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says Woof!")

# Create objects and call method
dog1 = Dog("Tommy", "Labrador")     # Object 1
dog2 = Dog("Rocky", "Pug")          # Object 2

dog1.bark()
dog2.bark()

Output:
       Tommy says Woof!
       Rocky says Woof!

'''
