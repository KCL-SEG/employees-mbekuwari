"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, salary):
        self.name = name
        self.contract = contract
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return self.name + " works on a monthly salary of " + str(self.salary) + ".  Their total pay is " + str(self.get_pay())+ "."

class Employee_hourly_nocommission:
    def __init__(self, name, contract, wage, hours):
        self.name = name
        self.contract = contract
        self.wage = wage
        self.hours = hours

    def get_pay(self):
        return self.wage * self.hours

    def __str__(self):
        return self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour. Their total pay is " + str(self.get_pay())+ "."

class Employee_salary_contract_commission:
     def __init__(self, name, contract, salary, contracts, contract_rate):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.contracts = contracts
        self.contract_rate = contract_rate

     def get_pay(self):
        return (self.salary) + (self.contracts*self.contract_rate)

     def __str__(self):
        return self.name + " works on a monthly salary of " + str(self.salary) + " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.contract_rate)+ "/contract.  Their total pay is "+ str(self.get_pay())+ "."

class Employee_hourly_contrac_commission:
     def __init__(self, name, contract, wage, hours, contracts, contract_rate):
        self.name = name
        self.contract = contract
        self.wage = wage
        self.hours = hours
        self.contracts = contracts
        self.contract_rate = contract_rate

     def get_pay(self):
        return (self.wage*self.hours) + (self.contracts*self.contract_rate)

     def __str__(self):
        return self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour and receives a commission for " + str(self.contracts)+ " contract(s) at " + str(self.contract_rate)+"/contract.  Their total pay is " + str(self.get_pay())+ "."

class Employee_salary_bonus:
    def __init__(self, name, contract, salary, bonus):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.bonus = bonus

    def get_pay(self):
        return self.salary+self.bonus

    def __str__(self):
        return self.name + " works on a monthly salary of " + str(self.salary) + " and receives a bonus commission of " + str(self.bonus)+".  Their total pay is " + str(self.get_pay())+ "."
        + str(self.get_pay())+ "."

class Employee_hourly_bonus:
     def __init__(self, name, contract, wage, hours, bonus):
        self.name = name
        self.contract = contract
        self.wage = wage
        self.hours = hours
        self.bonus = bonus

     def get_pay(self):
        return (self.wage*self.hours) + (self.bonus)

     def __str__(self):
        return self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour and receives a bonus commission of " + str(self.bonus)+ ".  Their total pay is " + str(self.get_pay())+ "."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000)

# # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee_hourly_nocommission('Charlie', "hourly", 25, 100)

# # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee_salary_contract_commission('Renee', "monthly", 3000, 4, 200)

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee_hourly_contrac_commission('Jan', "hourly", 25, 150, 3, 220)

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee_salary_bonus('Robbie', "monthly", 2000, 1500)

# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee_hourly_bonus('Ariel', "hourly", 30, 120, 600)
