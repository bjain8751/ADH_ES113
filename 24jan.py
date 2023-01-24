#Welcome to ADH!
#Code is updated on https://github.com/bjain8751/ADH_ES113
#Classes(Concepts and Hands on), Recursion(Concepts and Hands on), List(Implementation)


#bhavesh=student()

class student:

    def __init__(sur, name, rollno, age, marks):
        sur.name = name
        sur.rollno = rollno
        sur.age = age
        sur.marks = marks
    
    def age_marks(self):
        return(self.age+self.marks)

    def __repr__(self):
        return (f"Name: {self.name}, Roll No: {self.rollno}, Age: {self.age}, Marks: {self.marks}")

s1=student("Bhavesh", 1, 20, 100)
s2=student("Paras", 2, 22, 100)

print(s1.age_marks())

print(s1)




# def printhello():
#     print("Hello")


# printhello("HI")

#class point: (x,y,name) , distance from origin, print, distance from another point, add corresponding cordinates







