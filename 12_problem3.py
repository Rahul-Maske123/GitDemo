class Employee:
    salary = 5500
    increment = 1.4

    @property
    def salaryIncrement(self):
        return self.salary * self.increment

    @salaryIncrement.setter
    def salaryIncrement(self, sai):
        self.increment = sai/ self.salary

e = Employee()
print(e.salaryIncrement)


