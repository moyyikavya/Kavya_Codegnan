class university:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def main_details(self):
        print(f"Name      :{self.name}")
        print(f"Age       :{self.age}")
class students(university):
    def __init__(self,name,age,student_id,student_branch):
        super().__init__(name,age)
        self.student_id=student_id
        self.student_branch=student_branch
    def  student(self):
        print("__________student details__________")
        self.main_details()
        print(f"StudentID :{self.student_id}")
        print(f"Branch    :{self.student_branch}")
class proffesor(university):
    def __init__(self,name,age,ID,department):
        super().__init__(name,age)
        self.ID=ID
        self.department=department
    def employee(self):
        print("__________proffesor details__________")
        self.main_details()
        print(f"ID :{self.ID}")
        print(f"Department:{self.department}")
obj=students("kavya",19,"111","Bsc")
obj.student()
obj1=proffesor("kavya",19,"111","cs")
obj1.employee()
