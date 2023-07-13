# cars = ['bmw', 'mersedes', 'audi', 'byd', 'kia']
# cars.sort()
# print(cars)


# x = 10
# print(f'{x:b}')
# num_1 = int(input("Num1 : "))
  
# print(f'{num_1:x}')

# num_1 = int(input("Num1 : "),16)
# print(f'Hex: {num_1:x} \Dec : {num_1}')

# num_1 = int(input("Num1 : ") , 2)     
# print(f'Bin : {num_1:b} \n Dec : {num_1}')

# num_1 = int(input("Num1 : ") , b)     
# print(f'Bin : {num_1:b} \n Hex : {num_1:x}')

# x = 0b101
# y = 0x0a
# z = x + y
# sonni boshqa sanoq sistemasida formatlab chiqarish 
# print("in dec: {0} \n in binary :{0:5b} \n in hex {0:2x} \n in octal {0:2o}".format(y))


#     ---------Ro'yxatlar bilan ishlash---------

# mehmonlar = ['Abror' , 'Elyor' , 'Hasan' , 'Akrom' , 'Dilshod']
# print(f'sorted() qaytargan natija {sorted(mehmonlar )}')
# print(mehmonlar)
# mehmonlar.sort(reverse = True)
# print(mehmonlar)
# print (" Ro'yxat uzunligi : ",len(mehmonlar) )

# sonlar = list(range(0,10,1))
# juft_sonlar = list(range(0,10,2))
# toq_sonlar = list(range(1,10,2))

# print("Sonlar : ",sonlar)
# print("Juft sonlar ro'yxati : ",juft_sonlar)
# print("Toq sonlar ro'yxati : ",toq_sonlar)


# narxlar = [1000,2000,1250,2300,4000,5200,2400]

# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)

# print('eng arzon narx :',arzon ,'\neng qimmat narx : ', qimmat , '\njami narx :', jami)

# cars = ['Mers' , 'Volvo' , 'Kia' , 'Bmw' , 'tesla' , 'audi' , 'supra']

# my_cars = cars[0:3]

# print(my_cars)
# print(cars[:2])
# print(cars[4:])


# sonlar = list(range(0,21))
# sonlar_nus = sonlar[:]
# sonlar_nus.append(21)
# sonlar_nus.append(22)

# print(sonlar)
# print(sonlar_nus)





# products = ['potato' , 'garlic' , 'tomato' , 'onion']
# print(products)
# print(products[1])
# products[2] = 'carrot'
# print(products)

# print(len(products))
# print(len('hello'))

# products = ['potato' , 'garlic' , 'tomato' , 'onion']
# print(products)

# products.insert(2,'Kakos')
# print(products)

# products.append('turp')
# print(products)

# products.pop(2)
# print(products)

# products.remove('potato')
# print(products)


# products = ['potato' , 'garlic' , 'tomato' , 'onion']

# print(products)

# if 'potato' in products:
#     products.remove('potato')
# print(products)

# if 'potato' not in products:
#     products.append('potato')
# print(products)


# str1 = 'Hello World'
# lst1 = list(str1)

# print(lst1)

# lst2 = str1.split(' ')

# print(lst2)

# str2 = ','.join(lst2)
# print(str2)

# products = ['potato' , 'garlic' , 'tomato' , 'onion']

# print(products[int(input("qaysi elementni xoxlaysiz :"))-1])

# if 'potato' in products:
#     products.remove('potato')
# print(products)
# if 'potato' not in products:
#     products.insert(2,'potato')   
# print(products)


# 2 - qism 

# min()
# max()
# sum()

# lst = [i for i in range(10)]

# print(lst)
# print(min(lst))
# print(max(lst))
# print(sum(lst))


lst = [i for i in range(10)]

print(lst)
print(lst[2:7])
print(lst[0:2])
print(lst[-2::])