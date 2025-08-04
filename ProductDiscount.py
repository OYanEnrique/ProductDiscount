#Discount
product_price = float(input('Enter the price of the product:\n'))
final_price = 0.0
discount = 0.0
option = int(input('''Enter 1 to pay in cash
Enter 2 to pay in cash by card
Enter 3 to pay in 2 installments on your credit card 
Enter 4 to pay in 3 installments on your credit card 
'''))

if option == 1:
	discount = product_price * 0.10
	final_price = product_price - discount
	print('You got a 10% discount')
	print(f'The final price of this product is: {final_price}$')

elif option == 2:
	discount = product_price * 0.05
	final_price = product_price - discount
	print('You got a 5% discount')
	print(f'The final price of this product is: {final_price}$')
	
elif option == 3:
	final_price = product_price - discount
	print(f'The final price of this product is: {final_price}$')

elif option == 4:
	discount = product_price * 0.20
	final_price = product_price - discount
	print('You got a 20% discount')
	print(f'The final price of this product is: {final_price}$')

else:
	print('Invalid Option!')