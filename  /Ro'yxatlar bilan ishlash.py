#cars = ['mers','bmw','volvo','tesla']#\
#print(sorted(cars))
#sonlar = [12, 45, 23, 56, 998, 1, -5, -7.2]
#print(sorted(sonlar))


#sonlar = list(range(0,20,2))
#print(sonlar)


        # for 
#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']


#for mehmon in mehmonlar :
    
 #    print("Salom" , mehmon)
     
     
#for mehmon in mehmonlar :
  #  print(f"Hurmatli {mehmon} ,Sizni 20 dekabr kuni saylovga taklif qilamiz")
  
#sonlar = list(range(1,11))

#for son in sonlar:
  # print(f"{son} ning kvadrati : {son ** 2} ga teng")
  
#sonlar = list(range(1,11))
#sonlar_kv = []
#for son in sonlar: 
   # sonlar_kv.append(son**2)
#print(sonlar)
#print(sonlar_kv)    

# avtolar = [ 'audi ', 'bmw', 'volvo', 'kia', 'hyundai' ]
# for avto in avtolar:
#      if avto == 'bmw':
#       print(avto.upper())
#     else :
#       print(avto.title())




# =============================================================================
# ism = input('Ismingizni kiriting : ')
# 
# if ism.lower() != 'ali':
#     print(f'Uzr, {ism.title()} biz Alini kutyapmiz .')
# else :
#     print("Salo, Ali !")
# 
# 
# =============================================================================
# =============================================================================
# 
# 
# x,y = 50 , 40
# print("x>y") if x>y else print ("x<y")
# =============================================================================

# =============================================================================
# kun = input("Bugun kun nima : ")
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba':
#    print("Bugun dam olish kuni ")
# else :
#   print("ishlash kerak")
# 
# 
# 
# =============================================================================

# =============================================================================
# 
# narh = 15000
# 
# choy = True
# 
# salat = True
# 
# if choy and salat :
#  narh = narh + 10000
# elif choy or salat :
#  narh = narh + 5000
# 
# print(f'Sizdan {narh} so\'m bo\'ladi')
# 
# 
# 
# 
# 
# =============================================================================

# =============================================================================
# def summa(*sonlar):
#     '''Kiritilgan sonlar yig'indisini qaytaruvchi funksiya '''
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi 
# 
# 
# print(summa(1, 2))
# 
# print(summa(1, 2, 3, 4, 5, ))
# 
# 
# 
# =============================================================================
# =============================================================================
# 
# def summa(*sonlar):
#     '''Kiritilgan sonlar yig'indisini hisoblovchi funksiya '''
#     return sum(sonlar)
# 
# print(summa(2,3,4,5,6))
# 
# =============================================================================

# =============================================================================
# 
# def avto_info(kompaniya,model, **malumotlar):
#     '''Avto haqidagi malumotlarni lug'at 
#        ko'rinishida qaytaruvchi lug'at '''
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# 
# avto1 = avto_info('Gm', 'malibu', rang = 'qora', yil = 2020)
# avto2 = avto_info('Kia','K5',rang = 'qizil', narx = 35000)
# print(avto2)
# =============================================================================



def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rangi,
        'korobka': korobka,
        'yil': yili,
        'narx': narxi
    }
    return avto

def avto_kirit():
    '''Foydalanuvchi avto_info funksiyasi yordamida 
    bir nechta avtolar haqida ma'lumotlarni bitta 
    ro'yxatga joylash imkonini beruvchi funksiya'''
    avtolar = []
    
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end=' ')
        kompaniya = input('Ishlab chiqaruvchi: ')
        model = input('Modeli: ')
        rangi = input('Rangi: ')
        korobka = input('Korobka: ')
        yili = input('Ishlab chiqarilgan yili: ')
        narxi = input('Narxi: ')
        
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        
        javob = input('Yana avto qo\'shasizmi? (yes/no): ')
        if javob.lower() == 'no':
            break
    
    return avtolar

def info_print(avto_info):
    '''Avtomobillar haqida ma'lumotlar 
       saqlangan lug'atni konsolga chiqaruvchi funksiya'''
    print(f"{avto_info['rang'].title()}"
          f"{avto_info['kompaniya'].upper()}"
          f"{avto_info['model'].upper()}"
          f"{avto_info['korobka']} korobka,"
          f"{avto_info['yil']} - yil, {avto_info['narx']}$")
