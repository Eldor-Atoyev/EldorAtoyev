# def salom_ber(name):
#     ''' Salom beruvchi funksiya ''' 
#     print(f'Assalomu alaykum {name} !')

# salom_ber('Eldor')    

# def facto(n):
#   if n == 1:
#     return 1
#   return n * facto(n - 1)
# print(facto(2)) 


# 1
# def a_k(a , k):
#   for i in range(k):
#     for j in range(k):
#        print(f"{a}",end = '\t')
#     print('\n')
    
# a_k(4, 5)

# 2

# def sana(a , b):
#   for i in range(a,b+1):
#     if a <= b:
#      print(a)
#      a += 1
#   print(f" {i+1} ta son ")
     
# sana(0, 10)

# 3

# def kamay(a , b):
#   k = 0
#   for i in range(a,b-1):
#     k += 1
#     if b > a:
#      b -= 1
#      print(b)
     
#   print(f" {k} ta son ")
     
# kamay(20, 30)
# 4

# def konfet(a = 1):
#   konfet_kg = []

#   for i  in range (1,10):
#     s = a * i
#     konfet_kg.append(s)
#   return konfet_kg
  
# a = konfet(2000) 

# print(a)

# 5


# def konfet(a = 1):
#   konfet_kg = []

#   for i  in range (1,10):
#     s = a * i/10
#     konfet_kg.append(s)
#   return konfet_kg
  
# a = konfet(2000) 
# print(a)

# 6


# def konfet(a = 1):
#   konfet_kg = []

#   for i  in range (12,21,2):
#     s = a * i/10
#     konfet_kg.append(s)
#   return konfet_kg
  
# a = konfet(2000) 

# print(a)

# def summ(a,b):
#   s = 0 
#   for i in range(a,b+1):
#      s = s + a
#      a +=1
#   print(s)

# summ(1, 9)

# 1
# def power_3(a, b, C, *args, d):
#   lst_1 = [i ** 3 for i in args[0]]
#   return a ** 3, b ** 3, C ** 3, lst_1, float(d) ** 3

# print(power_3(1, 2, 3, [1, 2, 3, 4, 5], d=4.4))

# 2



