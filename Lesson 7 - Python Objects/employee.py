class Employee:
    def __init__(self, name, hourly_pay = 40):
        self.name = name
        self.pay = hourly_pay
        self.accumulated_hours = 0
    
    def add_work_hours(self, hours):
        self.accumulated_hours = self.accumulated_hours + hours
        
    def payday(self):
        due_pay = self.accumulated_hours * self.pay
        print(self.name, 'due pay is', due_pay)
        self.accumulated_hours = 0
        return(due_pay)
    
    def perc_raise(self, percentage):
        self.pay = self.pay * (1 + (percentage / 100))
        print(self.name, 'new hourly salary is', self.pay)