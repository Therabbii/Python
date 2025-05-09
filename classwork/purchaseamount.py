purchase_amount = int(input('Enter your purchase amount: '))

discount_amount = 0

if purchase_amount < 1000:
	print('No discount for this purchase amount. Sorry.')
elif purchase_amount >= 1000 and purchase_amount <= 10000:
	print('Discount of 5% will be added.')
	discount_percent = purchase_amount * 0.05
	discount_amount = purchase_amount - discount_percent
	print (f'Discounted purchase amount is  {discount_amount}')
elif purchase_amount >= 10001 and purchase_amount <= 50000:
	print('Discount of 10% will be added.')
	discount_percent = purchase_amount * 0.10
	discount_amount = purchase_amount - discount_percent
	print (f'Discounted purchase amount is  {discount_amount}')
elif purchase_amount > 50000:
	print('Discount of 20% will be added.')
	discount_percent = purchase_amount * 0.20
	discount_amount = purchase_amount - discount_percent
	print (f'Discounted purchase amount is  {discount_amount}')