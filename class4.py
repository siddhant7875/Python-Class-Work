#wap to get average of three number using class and object
class AverageCalculator:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_average(self):
        return (self.num1 + self.num2 + self.num3) / 3


# Input values
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Create an object of the class
calculator = AverageCalculator(num1, num2, num3)

# Calculate and display the average
average = calculator.calculate_average()
print(f"The average of the three numbers is: {average:.2f}")
