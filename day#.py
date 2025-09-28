# class Student: 
#   def __init__(self, name, year, enrolled, gpa):
#     self.name = name
#     self.year = year
#     self.enrolled = enrolled
#     self.gpa = gpa
  
#   def display_info(self):
#     print('The student ' + self.name + '\'s GPA is ' + str(self.gpa) + '!')

# mitsuha = Student('Mitsuha', 8, True, 3.8)
# taki = Student('Taki', 9, True, 3.6)

# mitsuha.display_info()
# taki.display_info()

# class Student: 
#   def __init__(self, name, year, enrolled, gpa):
#     self.name = name
#     self.year = year
#     self.enrolled = enrolled
#     self.gpa = gpa
  
#   def display_info(self):
#     print('The student ' + self.name + '\'s is ' + str(self.gpa) + '!')
  
#   def graduation(self):
#     if self.enrolled and self.gpa > 2.5 and self.year == 12:
#       print(self.name + ' will be able to graduate this year!')


class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"${self.balance}")

checking_account = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)

checking_account.deposit(100)

checking_account.display_balance()

checking_account.withdraw(50)

checking_account.display_balance()