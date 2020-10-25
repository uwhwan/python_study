from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    '''员工'''

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        '''结算月薪'''
        pass

class Manager(Employee):
    '''部门经理'''

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour

class Salesman(Employee):
    '''销售员'''

    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05

emps = [Manager('刘备'),Programmer('诸葛亮'),Manager('曹操'),
    Programmer('荀彧'), Salesman('吕布'), Programmer('张辽')]
for emp in emps:
    if isinstance(emp,Programmer):  #isinstance函数是判断员工对象的类型
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间：'))
    elif isinstance(emp,Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额：'))
    print(f'{emp.name}本月工资为：￥{emp.get_salary():.2f}元')
