principal_amount = int(input('Enter the principal amount for this investment: '))
number_of_years = int(input('Enter the number of years for this investment: '))
interest_rate = int(input('Enter the interest for this investment: '))

interest_rate = interest_rate / 100
interest_amount = interest_rate * principal_amount
return_on_investment = 0

for year in range(1, number_of_years + 1):
	for return_on_investment in (1, number_of_years + 1):
		return_on_investment = principal_amount + interest_amount
	print (f'ROI for year {year} is ₦{return_on_investment:,.2f}.')
	principal_amount = return_on_investment 
	interest_amount = interest_rate * principal_amount