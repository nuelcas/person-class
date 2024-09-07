# Define the 'Person' class
class Person:
    # Constructor method to initialize attributes when a new object is created
    def __init__(self, name, age, gender):
        # Initialize name, age, and gender for the person
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        # Print the introduction message with name, age, and gender
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the 'Person' class
person1 = Person("John Doe", 17, "Male")

# Call the 'introduce' method to display the person's information
person1.introduce()
