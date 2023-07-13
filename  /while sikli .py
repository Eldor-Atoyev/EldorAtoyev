# a = 1
# while a <= 5 :
#    print(a,end = ' ')
#    a += 1

# print('Kiritilgan sonning kvadratini qaytaruvchi dastur :')
# savol = 'Istalgan sonni kiriting '
# savol += "to'xtatish uchun 'exit' deb yozing : "
# qiymat = ''
# while qiymat != 'exit':
#      qiymat = input(savol)
#      if qiymat != 'exit':
#           print(float(qiymat) ** 2)

# print('Kiritilgan sonning kvadtarini hisoblovchi dastur : ')
# savol = 'Istalgan son kiriting '
# savol += '(to\'xtatish uchun \'exit\' deb yozing) :'
# ishora = True
# while ishora:
#      qiymat = input(savol)
#      if qiymat == 'exit' :
#           ishora = False
#      else :
#           print(float(qiymat) ** 2)



for i in range (1,11):
    for j in range (1,11):
        print(f"{i} * {j} = {i*j}",end="\t")
    print('\n')
        