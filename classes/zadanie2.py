class Employee:

    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.registered_normal_hours = 0
        self.registered_overhours = 0

    def register_time(self, hours):
        if hours > 8:
            self.registered_overhours = hours - 8
            self.registered_normal_hours = 8
        else:
            self.registered_normal_hours += hours

    def pay_salary(self):
        salary = self.registered_normal_hours * self.rate_per_hour + self.registered_overhours * self.rate_per_hour * 2
        self.registered_normal_hours = 0
        self.registered_overhours = 0
        return salary

employee = Employee("Jan", "Nowak", 100)

def test_employee_initialization():
    employee = Employee("Jan", "Kowalski", 100)

    assert employee.name == "Jan"
    assert employee.last_name == "Kowalski"
    assert employee.rate_per_hour == 100

def test_pay_salary_without_registered_time():
    employee = Employee("Jan", "Kowalski", 100)
    assert employee.pay_salary() == 0

def test_pay_salary():
    employee = Employee("Jan", "Kowalski", 100)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0

def test_pay_salary_over_hours():
    employee = Employee("Jan", "Kowalski", 100)
    employee.register_time(10)
    assert employee.pay_salary() == 800 + 400
    assert employee.pay_salary() == 0