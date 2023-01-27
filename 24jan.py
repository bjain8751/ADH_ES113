#Welcome to ADH!
#Code is updated on https://github.com/bjain8751/ADH_ES113
#Classes(Concepts and Hands on), Recursion(Concepts and Hands on), List(Implementation)


#bhavesh=student()
# class teacher:
    
#     def add_marksage(self):
#         return (self.marks+self.age)


# t1=teacher()
# t1.name="rohan"
# t1.age=20

# t1.marks=100



# class student:

#     def __init__(sur, name, rollno, age, marks):
#         sur.name = name
#         sur.rollno = rollno
#         sur.age = age
#         sur.marks = marks
    
#     def age_marks(sr):
#         return(sr.age+sr.marks)

#     def __repr__(self):
#         return (f"Name: {self.name}, Roll No: {self.rollno}, Age: {self.age}, Marks: {self.marks}")

# s1=student("Bhavesh", 1, 20, 100)
# s2=student("Paras", 2, 22, 100)

# print(s1.age_marks())


# print(s1)




# def printhello(a):
#     print(a)

# def printh(b):
#     print(a)
# print(printh(34))




# printhello("HI")

#class point: (x,y,name) , distance from origin, print, distance from another point, add corresponding cordinates


class point:
    def __init__(self, x, y, name):
        self.x=x
        self.y=y
        self.name=name

    def distance_from_origin(self):
        return (self.x**2+self.y**2)**0.5

    def __repr__(self):
        return (f"Name: {self.name}, X: {self.x}, Y: {self.y}")

    def distance_from_anotherpoint(a1, a2):
        return ((a1.x-a2.x)**2+(a1.y-a2.y)**2)**0.5

    def add_corresponding_cordinates(self, a2):
        return (self.x+a2.x, self.y+a2.y)
    
    def __add__(self, a2):
        return (self.x+a2.x, self.y+a2.y)


p2=point(2,3,"delhi")
p1=point(1,2,"mumbai")

print(p1.distance_from_origin())
print(p2.distance_from_origin())

print(p1)
print(p2)

print(p1.distance_from_anotherpoint(p2))

print(p1.add_corresponding_cordinates(p2))

print(p1+p2)





