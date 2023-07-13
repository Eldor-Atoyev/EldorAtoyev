# # car = {'model' : 'ferrari' , 'rang' : 'qora'}
# # print(car['model'])

# # talaba = {'ism': 'Murod olimov' , 'yosh': 20, 't_yil': 2000 }
# # print(f"{talaba['ism'].title()},\
# #     {talaba['t_yil']} - yilda tug'ilgan,\
# #     {talaba['yosh']} yoshda")


# car = {
#     'make': 'Gm',
#     'model': 'Malibu',
#     'color': 'Black',
#     'gear': 'automatic',
#     'year': '2020',
#     'price': '40000'
# }
# # print(f"Mashina narxi {car['price']}, so'm")

# narx = car.get('narx','Bunday kalit mavjud emas')

# # print(f"{car['narx']}")

# print(narx)

# onam = {
#     't_yil' : '1978',
#     't_shahar' : 'Bukhara',
#     'kasb' : 'o\'qituvchi'
# }

# otam = {
#     't_yil' : '1978',
#     't_shahar' : 'Bukhara',
#     'kasb' : 'quruvchi'
# }

# akam = {
#     't_yil' : '2001',
#     't_shahar' : 'Bukhara',
#     'kasb' : 'bukhgalter'
# }

# print(f"akam {akam['t_yil']} yilda, \
# {akam['t_shahar'].title()} viloyatida tug'ilgan \
# hozirda {akam['kasb'].title()} bo'lib ishlaydi !")

# taomlar = {
#     'vali' : 'osh',
#     'ali' : 'somsa',
#     'hasan' : 'sho\'rva',
#     'husan' : 'mastava',
#     'olim' : 'shashlik'
# }

# taom = taomlar['ali']

# print(f'Alining sevimli taomi : {taom}')

# python_izohli_lugati = {
#     'string' : 'matn',
#     'int' : 'Butun son',
#     'float' : 'o\'nlik son',
#     'list' : 'ro\'yxat',
#     'tuple' : 'bo\'sh ro\'yxat'
# }

#  print(python_izohli_lugati['tuple'])

# kalit = input('Biror bir so\'z kiriting').lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    

# kalit = input('Biror bir so\'z kiriting !').lower()
# print(python_izohli_lugati.get(kalit , 'Bunday qiymat mavjud emas ' ))

# kalit = input('Kalit so\' kiritng : ').lower()
# tarjima = python_izohli_lugati.get(kalit)

# if tarjima == None :
#     print('Bundsay so\'z mavjud emas')
# else :
#     print(f'{kalit.title()} so\'zi {tarjima} deb tarjima qilinadi')


# dictionaries = {
#     'olma' : 'apple,',
#     'uzum' : 'grapes',
#     'nok' : 'pear',
#     'behi' : 'quince',
#     'anor' : 'pomegranate',
#     'tarvuz' : 'watermelon'
# }


# kalit = input('Kalit so\'zni kiriting ! ').lower()
# print(dictionaries.get(kalit,'Bunday so\'z mavjud emas'))
# tarjima = dictionaries.get(kalit)

# if tarjima == None :
#     print('Bunday so\'z lug\'atda mavjud emas')
# else :
#     print(f'{kalit.title()} so\'zi {tarjima} deb tarjima qilinadi !')


# talaba = {
#     'ism' : 'alijon',
#     'familiya' : 'shamsiyev',
#     'yosh' : 22,
#     'fakultet' : 'matematika',
#     'kurs' : 4,
# }

# print(talaba.items())

# for kalit , qiymat in talaba.items() :
#     print(f'Kalit : {kalit}')
#     print(f'qiymat : {qiymat}')


# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s9' ,
#     'olim' : 'mi 10 pro',
#     'orif' : 'nokia 3310'
# }

# for k,q in telefonlar.items():
#   print(f'{k}ning telefoni : {q}')

# mahsulotlar = {
#     'olma' : '10000',
#     'anor' : '20000',
#     'uzum' : '40000',
#     'anjir' : '25000',
#     'shaftoli' : '30000'
# }
# print('Do\'kondagi mahsulotlar')
# for mahsulot in mahsulotlar:
#    print(mahsulot.title())

# bozorlik = ['anor' , 'uzum' , 'non' , 'baliq']
# for m in mahsulotlar :
#   if m in bozorlik :
#      print(f"{m.title()} {mahsulotlar[m]} so'm" )


# for mahsulot in sorted(mahsulotlar):
#   print(mahsulot.title())


# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s9',
#     'olim' : 'mi 10',
#     'orif' : 'nokia 3310'
# }
# for tel in sorted(telefonlar.values()):
#     print(tel)


# telefonlar = {
#     'ali' : 'iphone x',
#     'vali' : 'galaxy s9',
#     'olim' : 'mi 10 pro',
#     'orif' : 'nokia 3310',
#     'hamida' : 'galaxy s9',
#     'maryam' : 'huawei p30',
#     'tohir' : 'iphone x',
#     'umar ' : 'iphone x'
# }

# print('Foydalanuvchilarning telefonlari :')
# for tel in sorted(set(telefonlar.values())):
#     print(tel)

# talaba_0 = {
#     'ism' : 'alijon',
#     'familiya' : 'shamsiyev',
#     'yosh' : '24',
#     'fakultet' : 'matematika',
#     'kurs' : '3'
# }

# for kalit,qiymat in talaba_0.items():
#     print(f'kalit : {kalit}')
#     print(f"qiymat : {qiymat}")


# buxoriy = {
#     'ism' : 'Abu abdulloh ibn Ismoil ',
#     'tyil' : 810,
#     'vyil' : 870,
#     'tjoy' : 'buxoro',
#     'asarlar' : ["Al-jome' as-sahih", "Al-adab al-mufradot", "At-tarix al-kabir", "At-tarix as-sag'ir"]
# }

# qodiriy = {
#     'ism' : 'Abdulla Qodiriy',
#     'tyil' : 1894,
#     'vyil' : 1938,
#     'tjoy' : 'toshkent',
#     'asarlar' : ["O'tkan kunlar", "Mehrobdan Chayon", 'Obid ketmon']
# }

# vohidov = {
#     'ism' : 'Erkin Vohidov',
#     'tyil' : 1936,
#     'vyil' : 2016,
#     'tjoy' : "Farg'ona",
#     'asarlar' : ["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
# }

# navoiy = {
#     'ism' : 'Alisher Navoiy',
#     'tyil' : 1441,
#     'vyil' : 1501,
#     'tjoy' : 'Xirot',
#     'asarlar' : ["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
# }

# shaxslar = [buxoriy , qodiriy , vohidov , navoiy]

# for shaxs in shaxslar :
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     asarlar = shaxs['asarlar']
#     print(f"{ism} {tyil} - yilda {tjoy}da tavallud topgan,"
#           f" {vyil-tyil} yil umr ko'rgan \n ")    
#     for asar in asarlar:
#         print(f'{asar} ')
#     print('asarlarini yozgan\n')



# malibus = []

# for n in range(10):
#     new_car = {
#         'model' : 'malibu',
#         'rang' : None ,
#         'yil' : 2020,
#         'narx' : None,
#         'km' : 0,
#         'korobka' : 'avto'
#     }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang']='oq'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narx'] = 40000
#     else :
#         malibu['narx'] = 35000
# for malibu in malibus:
#     print(malibu.values())


# hamkasblar = {
# 'ali' :{'familiya' : 'valiyev',
#         'tyil' : 1995,
#         'malumot' : 'oliy',
#         'tillar' : ['python' , 'c++']        
#         },
    
# 'vali' :{'familiya' : 'aliyev',
#         'tyil' : 2001,
#         'malumot' : 'o\'rta maxsus',
#         'tillar' : ['html' , 'js' ,' css'] 
#         },
    
# 'hasan' :{ 'familiya' : 'husanov',
#         'tyil' : 1999,
#         'malumot' : 'maxsus',
#         'tillar' : ['python', 'php']
#         }
# }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()},"
#           f"{info['tyil']} - yilda tug'ilgan\n"
#           f"Ma'lumoti : {info['malumot']}.")
#     print("Quyidagi dasturlash tillarini biladi :")
#     for  til in info['tillar']:
#         print(til.upper())

