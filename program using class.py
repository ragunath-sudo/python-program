from stringprep import map_table_b3


class student:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def display(self):
        print("sno:",self.sno)
        print("name:",self.name)
        print("age:",self.age)
x=int(input("enter student no."))
y=input("enter student name.")
z=int(input("enter student age."))
object=student(x,y,z)
object.display()
class result:
    def __init__(self,a,b,c):
        self.m1=a
        self.m2=b
        self.m3=c
        self.total=a+b+c
    def display(self):
        print("m1:",self.m1)
        print("m2:",self.m2)
        print("m3;",self.m3)
        print("total",self.m1+self.m2+self.m3)
        print("avg:",self.total/3)
x=int(input("enter ur number"))
y=int(input("enter ur number"))
z=int(input("enter ur number"))
object=result(x,y,z)
object.display()