"""
1. declare variable principal and prompt the user for input
2. declare variable rate and prompt the user for input
3. divide the variable rate by 100 and then by the number of months
4. declare variable duration and multiply by number of months
5. declare variable numerator to calculate the numerator of the formula
6. declare variable denominator to calculate the denominator of the formula
7. declare variale monthlyPayment multiplying principal by the division of numerator and denominator
8. round the monthlyPayment into anoter variable payment to 2 decimal places
9. Print out the monthly payment
"""


principal = int(input("Enter the principal: "))

rate = float(input("Enter interest amount: "))

rate = (rate/100)/12
rateRound = round (rate , 4)
print ("Monthly rate will be " , rateRound)

duration = int(input("Enter duration in years: "))

duration = duration * 12
print("Duration in months is " , duration)

numerator = rate * (1 + rate) ** duration

denominator = (1 + rate) ** duration - 1

# monthlyPayment = principal * ( rate * (1 + rate) ** duration) / ( 1 + rate ) ** duration - 1)

monthlyPayment = principal * ( numerator / denominator )

payment = round (monthlyPayment , 2)

print("Your monthly payment is calculated to be $" , payment);

	
