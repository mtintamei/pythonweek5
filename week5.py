#Superhero Class with Inheritance and Polymorphism
# Base class - Superhero
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength

    def fight(self):
        print(f"{self.name} is fighting with {self.power} power!")

    def display_strength(self):
        print(f"{self.name} has a strength of {self.strength}.")

# Derived class - Flying Superhero (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, wingspan):
        super().__init__(name, power, strength)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with wingspan of {self.wingspan} meters!")

    def fight(self):
        # Polymorphism: Changing the behavior of the fight method
        print(f"{self.name} is fighting while flying with {self.power} power!")

# Derived class - Strength-Based Superhero (inherits from Superhero)
class StrengthBasedSuperhero(Superhero):
    def __init__(self, name, power, strength, weight_lifted):
        super().__init__(name, power, strength)
        self.weight_lifted = weight_lifted

    def lift(self):
        print(f"{self.name} can lift {self.weight_lifted} kg!")

    def fight(self):
        # Polymorphism: Changing the behavior of the fight method
        print(f"{self.name} is using strength to fight with {self.power} power!")

# Creating instances of each class
hero1 = Superhero("Superman", "Laser Vision", 100)
hero2 = FlyingSuperhero("Iron Man", "Repulsor Rays", 90, 20)
hero3 = StrengthBasedSuperhero("Hulk", "Gamma Radiation", 200, 1500)

# Using methods
hero1.fight()  # Output: Superman is fighting with Laser Vision power!
hero2.fight()  # Output: Iron Man is fighting while flying with Repulsor Rays power!
hero2.fly()    # Output: Iron Man is flying with wingspan of 20 meters!
hero3.fight()  # Output: Hulk is using strength to fight with Gamma Radiation power!
hero3.lift()   # Output: Hulk can lift 1500 kg!

#Activity 2: Polymorphism Challenge! 🎭
# Base class - Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class - Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived class - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create instances of each vehicle
vehicles = [Car(), Plane(), Boat()]

# Each vehicle will call its specific move method
for vehicle in vehicles:
    vehicle.move()

#Expected Output: Driving 🚗 Flying ✈️ Sailing ⛵

# Activity 3: Encapsulation Challenge 🛡️
# BankAccount Class with Encapsulation
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # Method to check balance (getter)
    def get_balance(self):
        return self.__balance

# Create an instance of BankAccount
account = BankAccount("John", 1000)

# Perform some operations
account.deposit(500)   # Depositing 500
account.withdraw(300)  # Withdrawing 300
print("Current balance:", account.get_balance())  # Accessing balance safely

# Expected Output:
# Deposited 500. New balance: 1500
# Withdrew 300. Remaining balance: 1200
# Current balance: 1200

