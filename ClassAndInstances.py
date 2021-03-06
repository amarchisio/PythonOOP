#Python Object-Oriented Programming

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jim', 'Smith', 50000)
emp_2 = Employee('John', 'Doe', 60000)


#Same way to print using the class.method and var=class.method
print (emp_1.fullname())
print (Employee.fullname(emp_1))
