#读取档案
products = []
with open('products.csv', 'r', encoding='utf-8')as f:
	for line in f:
		if 'Products, Price' in line:
			continue   #继续
		name, price = line.strip().split(',')
		products.append([name, price])
		
print(products)


while True:
	name = input('Insert Product Name: ')
	if name == 'q':
		break
	price = input('Insert Product Price: ')
	price = int(price)
	products.append([name, price])
print(products)	

for p in products:
	print('Product:', p[0], '  Price:', p[1])

with open('products.csv', 'w', encoding='utf-8')as f:
	f.write('Products, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
