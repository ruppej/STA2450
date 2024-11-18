# Exercise 2

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make},{self.model}"


class Inventory:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_inventory(self):
        for car in self.cars:
            print(car.description)


    def search_by_year(self, year):
        return [car.description() for car in self.cars if car.year == year]


car1 = Car("Toyota", "Sienna", 2009)

car2 = Car("Honda", "Accord", 2023)

car3 = Car("Toyota", "4Runner", 2022)

car4 = Car("Kia", "Sorento", 2008)


my_inventory = Inventory()

my_inventory.add_car(car1)
my_inventory.add_car(car2)
my_inventory.add_car(car3)
my_inventory.add_car(car4)

my_inventory.show_inventory()



# Exercise 4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
        self.classes_taught = []

    def display_prof_info(self):
        print(f"Name: {self.name}, Department: {self.department}")

    def add_course(self, course_name):
        self.classes_taught.append(course_name)
        print(f"Course {course_name} has been added to {self.name}'s courses")

    def list_courses(self):
        if self.classes_taught:
            print(f"{self.name} teaches the following courses: ")
            for course in self.classes_taught:
                print(f" - {course}")
        else:
            print(f"{self.name} has not added any courses yet.")


prof1 = Professor("John Smith", 45, "Computer Science")
prof1.display_info()
prof1.display_prof_info()

prof1.add_course("Data Structures")
prof1.add_course("Discrete Mathematics")
prof1.add_course("Java Programming")

prof1.list_courses()


