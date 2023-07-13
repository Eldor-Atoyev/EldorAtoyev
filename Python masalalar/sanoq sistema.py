# a = 0b101  # 5 o'nlikdagi qiymati
# # ushbu kodda 0b ikkilik sanoq sistemasini 101 esa 2likdagi sonni qiymatini bildiradi
# b = 0o10   # 10 o'nlikdagi qiymati
# ushbu kodda 0o sakkizlik sanoq sistemasini 10 esa 2likdagi sonni qiymatini bildiradi
# c = 0xb    # 15 o'nlikdagi qiymati 

# print(a, b , c)
# print(a+b+c)
# ----------------
# x = 0b101
# y = 0x0a
# z = x + y
# sonni boshqa sanoq sistemasida formatlab chiqarish 
# print("in dec: {0} \n in binary :{0:05b} \n in hex {0:02x} \n in octal {0:02o}".format(y))

# x = 10
# print(f'{x:b}')
# # yoki
# print('{0:b}'.format(x))

# name = "John"
# age = 30

# print("My name is {} and I'm {} years old hight ".format(name, age))


print(" \\\ Qaysi sanoq sistemalari o'rtasida konveyter qilmoqchisiz /// ")



print("\n Quyidagilardan birini tanlang: \n")


print("bin) ikkilik sanoq sistemasi ")


print("dec) O'nlik sanoq sistemasi ")


print("hex) o'n oltilik sanoq sistemasi\n")


sis_1 = input("Birinchi sanoq sistemasi : \n")


print(f" {sis_1} dan qaysi sanoq sistemasiga o'tkazmoqchisiz : \n")

print("dec) O'nlik sanoq sistemasi ")

print("bin) ikkilik sanoq sistemasi ")

print("hex) o'n oltilik sanoq sistemasi \n")

sis_2 = input("Ikkinchi sanoq sistemasi : \n")



if sis_1 == "dec" and sis_2 == "bin" :

    num_1 = int(input("Num1 : "))
    print(f'Dec : {num_1} \n Bin : {num_1:b}')

elif sis_1 == "dec" and sis_2 == "hex":

    num_1 = int(input("Num1 : "))
    print(f'Dec : {num_1} \n Hex : {num_1:x}')

elif sis_1 == "hex" and sis_2 == "dec":

   num_1 = int(input("Num1 : "),16)
   print(f'Hex : {num_1:x} \n Dec : {num_1}')

elif sis_1 == "hex" and sis_2 == "bin":   

    num_1 = int(input("Num1 : "),16)
    print(f'Hex : {num_1:x} \n Bin : {num_1:b}')


elif sis_1 == "hex" and sis_2 == "hex": 
    num_1 = int(input("Num1 : "),16)
    print(f"{num_1:x}")

elif sis_1 == "bin" and sis_2 == "hex":

   num_1 = int(input("Num1 : ") , 2)     
   print(f'Bin : {num_1:b} \n Hex : {num_1:x}')

elif sis_1 == "bin" and sis_2 == "dec":  

   num_1 = int(input("Num1 : ") , 2)     
   print(f'Bin : {num_1:b} \n Dec : {num_1}')

elif sis_1 == "bin" and sis_2 == "bin":
  num_1 = int(input("Num1 : ") , 2)  
  print(f'Bin : {num_1:b}')
elif sis_1 == "dec" and sis_2 == "dec": 
    num_1 = int(input("Num1 : "))
    print(f"{num_1}")
else :
    print("So'zlarni xato kiritdingiz")
