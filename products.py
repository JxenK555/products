import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8')as f:
		for line in f:
			if 'Products, Price' in line:
				continue   #继续
			name, price = line.strip().split(',')
			products.append([name, price])
	return products
	
#让使用者输入
def user_input(products):
	while True:
		name = input('Insert Product Name: ')
		if name == 'q':
			break
		price = input('Insert Product Price: ')
		price = int(price)
		products.append([name, price])
	print(products)	
	return products

#印出所有购买记录
def print_products(products):
	for p in products:
		print('Product:', p[0], '  Price:', p[1])

#写入档案
def write_file(filename,products):
	with open(filename, 'w', encoding='utf-8')as f:
		f.write('Products, Price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

#主要程式
def main():
	if os.path.isfile('products.csv'):
		print('This file has been found!')
		products = read_file('products.csv')
	else:
		print('Sorry, I dont see this file!')
		print('Type new products to create a new file.')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()