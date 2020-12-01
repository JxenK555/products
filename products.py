products = []
while True:
	name = input('Insert Product Name: ')
	if name == 'q':
		break
	price = input('Insert Product Price: ')
	products.append([name, price])
print(products)	

for p in products:
	print('Product:', p[0], ' Price:', p[1])