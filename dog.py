class Dog:

    country = "Japan"
    favourite_snack = "lettuce"
    number_of_friends = 0

    def __init__(self, breed, gender, colour, good_pet):
        self.breed = breed
        self.gender = gender
        self.colour = colour
        self.good_pet = good_pet
        Dog.number_of_friends += 1

    def bark(self):
        print(f"{self.breed} says Woof Woof Woof!")

    def wag_tail(self):
        print(f"{self.breed} wags its tail. Swish Swish Swish <3")


dog1 = Dog("Shiba", "male", "orange", True)
dog2 = Dog("Golden Retriever", "female", "cream", True)
dog3 = Dog("Doberman", "male", "black", True)
dog1.bark()
dog2.wag_tail()
print(Dog.number_of_friends)
print(dog1.breed)


class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def describe(self):
        print(f"this circle has {self.width}cm")


class circle(Shape):

    def __init__(self, width, height, filled, big):
        super().__init__(width, height)
        self.filled = filled
        self.big = big

    def describe(self):
        super().describe()
        print(f"this circle has {self.filled}cm")


circle = circle(width=35, height=20, filled=True, big=True)
circle.describe()


class Students:

    number_of_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Students.number_of_students += 1

    def get_info(self):
        return f"{self.name}, {self.grade}"

    @staticmethod
    def is_student(name):
        valid_students = ["Eugene", "May", "Ash", "Brock"]
        return name in valid_students

    @classmethod
    def class_method(cls):
        return Students.number_of_students


student1 = Students("Eugene", 5.2)
student2 = Students("Sandy", 5.2)
student3 = Students("May", 5.2)
print(Students.is_student("May"))
print(Students.number_of_students)
