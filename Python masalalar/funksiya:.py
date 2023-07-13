# for i in range (1,10):
#     for j in range (1,10):
#         print(str(i * j),end=" \t")
#     print('\n')

# def salom_ber(name):
#     print("Hello, "+name)
# salom_ber("Eldor")

# def info(str,int):
#     print(f'Name:  {str.title()}  Age :  {int} ')



# name = input('Ismingizni kiriting iltimos :')
# age = int(input('Yoshingizni kiriting iltimos :'))
# info(name, age)


# info(int = 20,str='Eldor')


# def summ(*params):
#     result = 0
#     for n in params:
#         result += n
#     return result

# b = 0

# while True: 
#     a = input('Son kiriting : ')
#     if a == 'a':
#         break
#     else:
#        a =int(a)
#        b =summ(b,a)
# print(b)

# def fact(a):
#     result =1
#     for n in range(1,a+1):
#         result *= n
#     return result
# print(fact(5))



# def salom_ber(ism):
#     ''' Salom beruvchi funksiya '''
#     print(f'Assalomu alaykum,hurmatli {ism.title()}!')


# def salom_ber(ism):
#     ''' Foydalanuvchi ismini qabul qilib,
#           unga salom beruvchi funksiya'''
#     print(f'Assalomu alaykum, hurmatli {ism.title()} !')
# salom_ber('eldor')


# def toli_ism(ism,familiya):
#     ''' Ism va familiyani jamlab chiqaruvchi funksiya '''
#     print(f'Foydalanuvchi ismi {ism.title()}\n'
#           f'Foydalanuvchi familiyasi {familiya.title()}')
    
    
# toli_ism('eldor','atoyev')    
    
    
# def yosh_hisobla(ism,tugilgan_yil):
#     ''' Foydalanuvchi yoshini hisoblaydigan funksiya '''
#     print(f'{ism.title()} {2023-tugilgan_yil} yoshda')
    
# yosh_hisobla('eldor', 2003)
    
    
# def yosh_hisobla(tugilgan_yil,joriy_yil = 2023):
#     print(f'Siz {joriy_yil - tugilgan_yil} yoshdasiz')

# yosh_hisobla(2003,2024)

# def yosh_hisobla(tugilgan_yil, joriy_yil = 2023):
#  '''Tug'ilgan yildan yoshini hisoblaymiz '''
#  print(f'Siz {joriy_yil - tugilgan_yil} yoshdasiz')
 
 
 
# tyil = int(input('Tug\'ilgan yilingizni kiriting : '))
 
# yosh_hisobla(tyil)

# def tugilgan_yil(ism,yosh):
#     '''Foydalanuvchi tug'ilgan yilini hisoblaydigan dastur '''
#     print(f'{ism} {2023 - yosh} yilda tugilgan')

# tugilgan_yil('Eldor', 20)
# def daraja(son):
#     ''' Sonning kvadrati va kubini hisoblovchi dastur ''' 
#     print(f'{son} ning kvadrati : {son ** 2} \n'
#           f'{son} ning kubi : {son ** 3}')
    
# daraja(4)
    
# def daraja(son,dar):
#     '''Sonning darajasini hisoblovchi dastur '''
#     print(f'{son} ning {dar} inchi darajasi : {son ** dar}')
    
# daraja(2,-2)


# def son(n):
#     if n % 2 == 0:
#         print("Son juft son")  
#     else:
#         print('Son toq son')

# son(2)

# def taqqosla(son1,son2):
#     if son1 > son2 :
#       print(f"{son1} eng katta son")
#     elif son2 > son1 :
#       print(f"{son2} eng katta son")
#     else :
#       print('Ikki son teng !!!')
# taqqosla(2, 4)

# def dar(son,n = 2):
#     ''' Sonning n inchi darajasini hisoblovchi dastur '''
#     print(f'{son} ning {n} inchi darajasi : {son ** n} ga teng')
  
# dar(2)

# def qoldiqsiz(a):
#     for i in range(2,11):
#       if a % i == 0:
#           print(f'{a} {i} ga qoldiqsiz bo\'linadi')
#       else :
#         print('Siz tub son kiritdingiz !!!')
#         break
# qoldiqsiz(113)



# print('Do\'stlaringizni yoshinni saqlaymiz.')

# dostlar = {}

# ishora = True

# while ishora:
#     ism = input('Do\'stingizni ismini kiriting :')
#     yosh = input(f'{ism.title()}ning yoshini kiriting :') 
#     dostlar[ism] = int(yosh)
#     javob = input('Yana ma\'lumot qo\'shasizmi? (ha/yo\'q) ')
#     if javob == 'yo\'q':
#         ishora = False
    
    

# def toliq_ism_yasa(ism , familiya , otasining_ismi = ''):
#    ''' To'liq ism yasovchi  funksiya '''
#    if otasining_ismi :
#        toliq_ism = f'{ism} {otasining_ismi} {familiya}'
#    else:
#        toliq_ism = f'{ism} {familiya}'
#    return toliq_ism.title()
       
       
# talaba1 = toliq_ism_yasa('Eldor', 'Atoyev','Erkin o\'g\'li')
# talaba2 = toliq_ism_yasa('hakim', 'olimov' ,'abrorovich')
# print(f'darsga kelmagan talabalar : {talaba1} va {talaba2}')

   
# def avto_info(make, model, rangi, korobka, yili, narxi = None):
#     avto = {'kompaniya' : make,
#             'model' : model,
#             'rang' : rangi,
#             'korobka' : korobka,
#             'yil': yili,
#             'narx': narxi}
#     return avto

# avto1 = avto_info('Gm', 'Malibu', 'Qora', 'Avtomat', '2018')
# avto2 = avto_info('Gm', 'Gentra', 'OQ', 'Mexanika', '2016',15000)
# avtolar = [avto1, avto2]

# print('Onlayn bozordagi mavjud avtomashinalar : ')
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = 'Noma\'lum'
#     print(f"{avto['rang']} {avto['model']}.Narxi : {narx}")

# def oraliq(min,max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0, 10))



# print(" Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []
# while True:

#     print("\nQuyidagi ma'lumotlarni kiriting :", end='\n')
#     kompaniya = input("Ishlab chiqaruvchi :")
#     model = input('Modeli: ')
#     rangi = input('Rangi : ')
#     korobka= input('Korobka : ')
#     yili = input("Ishlab chiqarilgan yili : ")
#     narxi = input("Narxi :")
#     #Kiritilgan ma'lumotlarni avto_info yordamida
#     #lug'at shakllantirib , ro'yxatga qo'shamiz
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili,narxi))
    
#     #Yana avto qo'shish qo'shmasligini so'raymiz
    
#     javob = input('Yana avto qo\'shasizmi ? (yes/no): ') 
#     if javob == 'no':
#       break
  
  
# def bahola(ismlar):
#  baholar = {}
#  while ismlar :
#      ism = ismlar.pop()
#      baho = input(f'{ism.title()}ning bahosini kiriting : ')
#      baholar[ism] = baho
#  return baholar


# talabalar = ['Ali', 'Vali' , 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)  



    
  
  