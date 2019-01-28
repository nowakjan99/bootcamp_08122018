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

        temp = (self.registered_normal_hours * self.rate_per_hour + self.registered_overhours * self.rate_per_hour * 2)
        self.registered_normal_hours = 0
        self.registered_overhours = 0

        return temp

class PremiumEmployee(Employee):
    def __init__(self, name, last_name, rate_per_hour):
        super().__init__(name, last_name, rate_per_hour)
        self.bonuses = 0
    def pay_salary(self):
        temp = self.bonuses
        self.bonuses = 0
        return super().pay_salary() + temp
    def give_bonus(self, amount):
        self.bonuses += amount

employee = PremiumEmployee("Jan", "Nowak", 100)
employee.register_time(5)
employee.give_bonus(1000)
print(employee.pay_salary())
