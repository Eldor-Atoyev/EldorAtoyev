
#1 jut sonmi ?
# a = int(input("Son : "))

# print(f"Son musbtami :{a>0}")


#2 Toq sonmi ?

# a = int(input("Son : "))

# print(f"Son musbtami :{a>0}")

#3 Juft sonmi ?

# a = int(input("Son : "))
# print(f'Juft sonmi : {a % 2 == 0}')

#4 a > 2 va b <= 3

# a = int(input('A : '))
# b = int(input('B : '))

# print(f'A > 2 va B <= 3 :  {a > 2 and b <= 3}')

#5 a >= 0  yoki b < -2

# a = int(input('A : '))
# b = int(input('B : '))

# print(f'A >=0 va B < -2 :  {a >= 0 or b < -2}')

#6 A<= В <= С

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f'A <= B <= C :  {a <= b and b <= c}')


#7 A < В < С

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f'A < B < C :  {a < b and b < c}')

#8 A va B sonlar toq sonlar
 
# a = int(input('A : '))
# b = int(input('B : '))


# print(f" A va B sonblari toq sonlar \
#     {a % 2 != 0 and  b % 2 != 0}")

#9 A va B sonlarining hech bo'lmasa bittasi toq son
 
# a = int(input('A : '))
# b = int(input('B : '))


# print(f" A va B sonlarining hech bo\'masa bittasi toq son \
#     {a % 2 != 0 or  b % 2 != 0}")


#10 A va B sonlarining faqat bittasi toq son
 
# a = int(input('A : '))
# b = int(input('B : '))


# print(f" A va B sonlarining faqat bittasi toq son \
#     {(a % 2 != 0 and  b % 2 == 0) or (a % 2 == 0 and  b % 2 != 0)}")



#11 A va B sonlarining har ikkalasi ham toq son yoki juft son 
 
# a = int(input('A : '))
# b = int(input('B : '))


# print(f"A va B sonlarining har ikkalasi ham toq son yoki juft son  \
#     {(a % 2 != 0 and  b % 2 != 0) or (a % 2 == 0 and  b % 2 == 0)}")

#12 A  В  С sonlarining har biri musbat son :

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f' A B C sonlarining har biri musbat son : \
#     {a > 0 and b > 0 and c > 0}')


#13 A  В  С sonlarining hech bo'lmasa bittasi musbat son :

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f' A B C sonlarining har biri musbat son : \
#     {a > 0 or b > 0 or c > 0}')


#14 A  В  С sonlarining faqat bittasi musbat son :

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f' A B C sonlarining faqat bittasi musbat son : \
#     {(a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0)  }')


#15 A  В  С sonlarining faqat iktasi musbat son :

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f' A B C sonlarining faqat bittasi musbat son : \
#     {(a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c > 0)  }')

# 16  “Berilgan son ikki xonali juft son".

# a = int(input(" A : "))

# print(f'Berilgan son ikki xonali juft son : {99 >= a >= 10 and a % 2 == 0}')


# 17  “Berilgan son uch xonali toq son".

# a = int(input(" A : "))

# print(f'Berilgan son uch xonali toq son : {999 >= a >= 100 and a % 2 != 0}')

#18 "Berilgan uchta butun sonlarning hech bo’lmaganda 2 tasi bir birigateng". 

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f'Berilgan uchta butun sonlarning hech bo’lmaganda 2 tasi bir birigateng".\
#     {a == b != c or a != b == c or a == c != b }')


#19 “Berilgan uchta butun sonlarning hech bo’lmaganda bir jufti o’zaro qarama-qarshi". 

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

# print(f'Berilgan uchta butun sonlarning hech bo’lmaganda bir jufti o’zaro qarama-qarshi.\
#     {a == -b != c or a != b == -c or a == -c != b }')
    
# 20 Berilgan  uch xonali sonning raqamlari har xil

# a = int(input('A : '))

# a100 = a // 100 
# a10  = a // 10 % 10 
# a1   = a % 10  

# print ( a100 != a10 and a10 != a1 and a100 != a1)