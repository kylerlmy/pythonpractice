# coding=UTF-8

class SchoolMember:
    '''代表任何学校里的成员'''
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print('(Initialized SchoolMember:{})'.format(self.name))

    def tell(self):
        ''' 告诉有关我的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=' ')


class Teacher(SchoolMember):
    ''' 代表一位老师'''

    def __init__(self, name, age,salary):
        SchoolMember.__init__(self,name, age) #调用基类方法时，第一个参数也必须为 self
        self.salary=salary
        print('(Initialized Teacher:{})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self) #调用基类方法时，第一个参数也必须为 self
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    ''' 代表一个学生'''

    def __init__(self, name, age,marks):
        SchoolMember.__init__(self,name, age)
        self.marks=marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

class Work(SchoolMember):
    ''' 学校的其他工作人员 '''
    def __init__(self, name, age,comefrom):
        super().__init__(name, age) #通过 super() 方法调用基类方法时，不需要再将第一个参数指定为 self
        self.comefrom=comefrom

    def tell(self):
        super().tell()              #通过 super() 方法调用基类方法时，不需要再将第一个参数指定为 self
        print('Come From:"{}"'.format(self.comefrom))


m=SchoolMember('John',23)
t=Teacher('Mrs.Li',40,3000)
s=Student('Kyle',25,75)
w=Work('Tom',34,'Japana')

print()

members=[m,t,s,w]

for member in members:
    # 全体师生都要执行
    member.tell()
        
