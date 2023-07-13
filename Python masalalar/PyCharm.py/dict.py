# lugat = {
#     'ism':'Abror',
#     'familiya':'Aliyev',
#     '12': 'qwee '
# }
# print(lugat)
# key -> immutable(o'zgarmas)
#  int ,str, bool, float
# value -> farqi yo'q
# farqi yo'q
# d = {
#     12.23: 12,
#     43:44,
# }
#
# print(d)

# dct = {12 : 23 , 43 : 44 , 'son' : 'eartret'}

# 2  operatsiyalar


# print(dct)
#
# dct[12] = 'update'
# print(dct['son'])
# dct['asd'] = 'asd'
# print(dct)
#
# dct = {12 : 33 , 43 : 44 , 'son' : 'eartret'}
# dct2 = {"qwerty" : 45}
#
# dct.update(dct2)
# print(dct)

# lugat = {
#     "olma" : 12_000,
#     "anor" : 15_000,
#     'uzum' : 20_000,
#     'anjir': 25_000
# }
#
# lugat2 = {'banan': 14_000}
# lugat.update(lugat2)
# print(lugat)
#

# buyumlar = {
#     'meva' : 'olma',
#     'sabzavot' : 'sabzi',
#     'texnika' : 'kompyuter',
#     'narx' : '20_000'
# }
#
# # buyumlar['dastur'] = 'python'
#
# binolar = {
#     'turi' : 'gishtli',
#     'narx': 40_000
# }
#
# buyumlar.update(binolar)
# print(buyumlar)


 # masala.

# if "meva" in buyumlar :
#     print(buyumlar['meva'])
# if 'sabzavot' in buyumlar :
#     print(buyumlar['sabzavot'])
# if 'kalit' in buyumlar :
#     print(buyumlar['kalit'])

# buyumlar = {
#     'meva' : 'olma',
#     'sabzavot' : 'sabzi',
#     'texnika' : 'kompyuter',
#     'narx' : '20_000'
# }


# print(buyumlar.get('meva2') , buyumlar['meva'])

# built in funksiyalar len(), type(), isinstance()

# print(isinstance(buyumlar, dict))
#
#
# buyumlar = {
#     'meva' : 'olma',
#     'sabzavot' : 'sabzi',
#     'texnika' : 'kompyuter',
#     'narx' : '20_000'
# }
#
#
# d1 = {'a' : 100, 'b' : 200 , 'c' : 300}
# d2 = {'a' : 300, 'b' : 250 , 'd' : 400  }
# res = {}
#
# for key, value in d1.items():
#     if key in d2 :
#         d1[key] += d2.pop(key)
# d1.update(d2)
#

# def search(dct : Dict, values: List )->List:

# students = {
#     'Abror' : 66,
#     'Jamshid' : 78,
#     'Rustam' : 86,
#     'Ali' : 60,
#     'Vali' : 90,
#     'Alisher' : 86,
#     'Soli' : 66,
#     'Jamshid' : 83,
#     'Rustam' : 89,
# }


# def asii_qaytar(char):
#     return ord(char)
# print(asii_qaytar(''))


# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
#
# sorted_d = sorted(d.items(),key=operator.itemgetter(1))
#
# print('Dictionary in ascending order by value : ',sorted_d)




def solution( nums,a):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
          if j - i == a and i < j:
             for k in range(len(nums)) and j < k:
                  if k - j == a :
                      count +=1

    return count

nums = [0, 1, 4, 6, 7, 10]

print(solution(nums))