class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def calculate_total(self):
        return self.m1 + self.m2

    def __add__(self, student):
        """ add method overloading"""
        a = self.m1 + student.m1
        b = self.m2 + student.m2

        return a, b

    def __gt__(self, other):
        """ Greater than method overloading"""
        student1 = self.calculate_total()
        student2 = other.calculate_total()

        if student1 > student2:
            return True
        else:
            return False


s1 = Student(62, 78)
s2 = Student(87, 56)

print(s1.calculate_total())
print(s2.calculate_total())

if s1 > s2:
    print('s1 is greater then s2')
else:
    print("s2 is greater than s1")

print(f"Adding two student : {s1 + s2}")