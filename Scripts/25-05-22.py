#oop
import math
import random

class Human:

	def __init__(self, name, age, cash):
		self.name = name
		self.age = age
		self.cash = cash

	def __str__(self):
		return f"{self.name} - {self.age}"

	def get_cash(self):
		return self.cash

class BankAccount:

	number = f"{random.randint(int(math.pow(10, 8)), int(math.pow(10, 9)))}-{random.randint(int(math.pow(10, 8)), int(math.pow(10, 9)))}-{random.randint(int(math.pow(10, 8)), int(math.pow(10, 9)))}"


	def __init__(self, money, human):
		self.money = money
		self.human = human
		self.name = self.human.name

	def withdraw(self, amount):
		if self.money > amount:
			self.money -= amount*1.02
			print(f"Szia bátyus megloptak {f'{amount:,d}'.replace(",", ".")} pénzecskével hahaha")
			self.human.cash+=amount
		else:
			print(f"Csóró vagy bátyus")

	def add(self, amount):
		self.money+=amount
		self.human.cash-=amount*1.02
		print(f"Szia bátyus de sok pénzed van korrupt politikus vagy? {f'{self.money:,d}'.replace(",", ".")}")

mintamarci = Human("Minta Márton", 42, 10000)
mintamarcibank = BankAccount(6000000000, mintamarci)

mintamarcibank.withdraw(2000000)
print(mintamarci.cash)
print(mintamarcibank.money)
print(mintamarcibank.number)