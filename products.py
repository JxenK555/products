import os #operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):   #檢查檔案在不在
	print('This file has been found.')
	with open('products.csv', 'r', encoding='utf-8')as f:
		for line in f:
			if 'Products, Price' in line:
				continue   #继续
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('Sorry, I dont see this file!')
	print('Type in the blank to create a new file')

#让使用者输入
while True:
	name = input('Insert Product Name: ')
	if name == 'q':
		break
	price = input('Insert Product Price: ')
	price = int(price)
	products.append([name, price])
print(products)	

#印出所有购买记录
for p in products:
	print('Product:', p[0], '  Price:', p[1])

#写入档案
with open('products.csv', 'w', encoding='utf-8')as f:
	f.write('Products, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
