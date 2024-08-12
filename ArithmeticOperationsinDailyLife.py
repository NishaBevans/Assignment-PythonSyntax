#Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!

bread = 2.00
milk = 2.45
cheese = 4.75
#attempted to use sum(); raised TypeError: sum() takes at most 2 arguments (3 given)
numbers = 2.00, 2.45, 4.75
total = sum(numbers)
print(total)

#Task 2: Bank Interest If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

initial_investment = (10000)
rate = (0.07)
years = 1
final_value = initial_investment * (1 + rate) ** years
print(final_value)
