# from zadanie2 import Employee

class Employee:

    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.__registered_normal_hours = 0
        self.registered_overhours = 0

    def register_time(self, hours, ):
        # if hours > 8:
        #     self.registered_overhours = hours - 8
        #     self.registered_normal_hours = 8
        # else:
        #     self.registered_normal_hours += hours

        if hours > 8:
            self.__registered_normal_hours += 8 + (hours - 8) * 2
        else:
            self.__registered_normal_hours += hours


    def pay_salary(self):
        salary = self.__registered_normal_hours * self.rate_per_hour + self.registered_overhours * self.rate_per_hour * 2
        self.__registered_normal_hours = 0
        self.registered_overhours = 0
        return salary

class PremiumEmployee(Employee):

    def __init__(self, name, last_name, rate_per_hour):
        super().__init__(name, last_name, rate_per_hour)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount

    def pay_salary(self):
        to_pay = super().pay_salary() + self.bonus
        self.bonus = 0
        return to_pay

def test_premium_employee_give_bonus():
    employee = PremiumEmployee("Jan", "Słodowy", 100)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500
    assert employee.pay_salary() == 0