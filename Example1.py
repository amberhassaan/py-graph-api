"""
Example 1: shows the use of add/get/remove properties and value-based projection

There are two classes: Course and Student. Course is a set of Students.
Abstractly, we can think of a Course as a graph in which the nodes are Students
and there are no edges. 

Student has
  - name
  - isGrad: true if student is a grad student and false otherwise
Code shows a property named "age" being added, read, and removed

Course has 
  - set of students, all of whom are of the same type Student
  - course ID
Code shows a projection of a Course to create a Course with grad students or undergrad students only
"""

class Student:
    name: str
    isGrad: bool
    def __init__(self, naam: str, grad: bool):
        self.name = naam
        self.isGrad = grad
        
    def add_property(self,prop:str,value:any):
        setattr(self,prop,value)
        print("Adding property \"" + prop + "\" with value " + str(value))
        
    def get_property(self,prop:str):
        if hasattr(self,prop): return getattr(self,prop)
        else: return "No property called \"" + prop + "\" exists"
        
    def remove_property(self, prop:str):
        if hasattr(self,prop): 
            delattr(self,prop)
            print("Removing property \"" + prop + "\"" )
        else: return "No property called " + prop + " exists"
        
s1 = Student("Aaron", False)
print(s1.name, s1.isGrad)
s1.add_property("age",23)
print(s1.name,getattr(s1,"age"))
s1.remove_property("age")
print(s1.get_property("age"))

"""
***************************************************************
Output:
Aaron False
Adding property "age" with value 23
Aaron 23
Removing property "age"
No property called "age" exists

***************************************************************
"""

class Course:
    students: [Student]
    courseID: str
    def __init__(self,people:[Student],uid: str):
        self.students = people
        self.courseID = uid
        
    def enrollment(self):
        print("Students enrolled:")
        for s in self.students:
            print(s.name + " ")
    
    # value-based projection
    def project(self, level: str, courseID: str):
        sub = []
        if (level == "grads"):
            for s in self.students:
                if (s.isGrad): sub.append(s)
        else:
            if (level == "undergrads"):
                for s in self.students:
                    if (not s.isGrad): sub.append(s)
            else:
                print("Invalid level " + level)
        subCourse = Course(sub,courseID)
        return subCourse
                    
            
            
s2 = Student("Sandy",True)
C = Course([s1,s2],"cs361")
print(C.enrollment())
C2 = C.project("grads", "CS371")
print(C2.enrollment())

"""
*****************************************
Output:

Students enrolled:
Aaron 
Sandy 
None
Students enrolled:
Sandy 
None
"""
