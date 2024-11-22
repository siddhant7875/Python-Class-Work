#Wap to get simple interest using class and object
class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_interest(self):
        return (self.principal * self.rate * self.time) / 100


# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

# Create an object of the class
calculator = SimpleInterestCalculator(principal, rate, time)

# Calculate and display the Simple Interest
interest = calculator.calculate_interest()
print(f"Simple Interest is: {interest:.2f}")
