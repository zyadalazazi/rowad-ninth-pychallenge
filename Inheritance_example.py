"""
This is a simple program that implements the basics of OOP:
- Classes and objects
- Constructors and Destructors
- Inheritance
- Access Modifiers
- Encapsulation
- Polymorphism
- Abstraction
"""

# Creating a class called Person with two protected attributes and one private attribute
class Person:

    # Creating a constructor
    def __init__(self, name: 'str', age: 'int'):
        self._name = name  # protected attribute can be accessed by the objects of the superclass and subclass
        self._age = age  # protected attribute can be accessed by the objects of the superclass and subclass
        self.__job = "No job"  # private attribute can only be accessed by objects of type Person

    # An example on abstraction
    def __str__(self):
        return "The person's name is {0}, their age is {1} and their job is {2}".format(self._name, self._age, self.__job)

    # Creating a destructor
    def __del__(self):
        print("The person {0} has been deleted".format(self._name))

    # An example of encapsulation (the private attribute cannot be changed except through this function)
    def set_job(self, new_job: 'string'):
        self.__job = new_job


# The inheritance occurs as the class Student (subclass) inherits from the class Person (superclass)
class Student(Person):

    # Creating a constructor
    def __init__(self, name: 'str', age: 'int', student: 'boolean'):
        super().__init__(name, age)
        self.student = student

    # An example of polymorphism as the implementation is different from the one in the parent class
    def __str__(self):
        if self.student:
            return "The student's name is {0} and their age is {1}".format(self._name, self._age)
        else:
            # This inherits the work of the function in the superclass
            return super().__str__()

    # Creating a destructor
    def __del__(self):
        if self.student:
            print("The student {0} has been deleted".format(self._name))
        else:
            # This inherits the work of the function in the superclass
            print(super().__del__())


"""
This is the main program that the user sees
"""

# We create three objects to show the differences
student1 = Student("Fadi", 14, True)  # object of type Student
student2 = Student("Abdo", 33, False)  # object of type Person but instantiated as a Student
person1 = Person("Fatima", 44)  # object of type Person

"""
The print() statements are an example of abstraction as the user does not know
how it is implemented on the Person and Student classes
"""
print(student1)
del student1
print()

print(student2)
del student2
print()

print("Before job change:", person1)
person1.set_job("Engineer")
print("After job change:", person1)
del person1
