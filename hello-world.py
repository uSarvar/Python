# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:24:43 2021

@author: Sarvar
"""

#print('Hello world!')

#print('mening yoshom', 3*9, 'da')
#print("Biz kelib-ketguvchi to'garak jahon,\nNa boshi ma'lumu na so'ngi ayon,\nHech kim rostini aytib berolmas,\nQaydan keldigu, keturmiz qayon.")
#print(25//6)
#print("\"Nexia\", \"Tico\", 'Damas' ko\'rganlar qilar havas")
# 5 ning 4-darajasini toping
#print(5**4)

# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
#print(22%4)

# Diametri 12 ga teng bo'lgan doiraning yuzini toping  (pi=3.14 deb oling)
#print(3.14*6**2)
# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
#print((6**2+7**2)**(1/2))

#salom = 'Hello World!'
#print(salom)
#xabar = 'bu Pythondagi yangi xabar'
#print(xabar)
#radius = 10
#pi = 3.14159
#aylana_yuzi = pi*radius**2
#print('Aylananing radius', radius, 'ga va yuzi =', aylana_yuzi, 'ga teng.')


#ism = 'james'
#familiya = 'bond'
#ism_sharif = f"{ism} {familiya}"
#print(ism_sharif)
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.capitalize())
#print(ism_sharif.title())
#print(f"Salom mening ismim {familiya}, {ism} {familiya}")

#matn = 'bugun havo juda ajoyib, tashqarida qor yog\'moqda 🌨'
#print(matn)

#meva = '       olma      '
#print(meva)
#print('Men '+meva.lstrip()+' mevasini yaxshi ko\'raman')
#print('Men '+meva.rstrip()+' mevasini yaxshi ko\'raman')
#print('Men '+meva.strip()+' mevasini yaxshi ko\'raman')

#ism = input('Ismingizni kiriting\n=> ')
#print('Salom '+ism)
#print('Assalomu alaykum '+ism.title()+'!')

#kocha = 'Bo\'gbon'
#mahalla = 'Sog\'bon'
#tuman = 'Bodomzor'
#viloyat = 'Samarqand'
#print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+' tumani, '+viloyat+' viloyati.')

#kocha = input("Ko'changiz nomini kiriting:\n")
#mahalla = input("Mahallangiz nomini kiriting:\n")
#tuman = input("Tumaningiz nomini kiriting:\n")
#viloyat = input("Viloyatingiz/Shahringiz nomini kiriting:\n")

#print('Manzilingiz: ',kocha,' ko\'chasi, ',mahalla,' mahallasi, ',tuman,' tumani, ',viloyat,' viloyati/shahri.')

#manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."
#print(manzil.title())


#son = int(input('Istalgan son kiriting\n=>'))
#print(son,' ning kvadrati ',son**2,' ga teng')
#print(son,' ning kubi ',son**3,' ga teng')

#f_yili = int(input("Tug'ilgan yilingizni kiriting: "))
#yoshi = 2021 - f_yili
#print('Siz ',yoshi,' yoshdasiz')

#son1 = int(input("1-sonni kiriting: "))
#son2 = int(input("2-sonni kiriting: "))

#print(f"{son1} + {son2} =",son1+son2)
#print(f"{son1} - {son2} =",son1-son2)
#print(f"{son1} * {son2} =",son1*son2)
#print(f"{son1} / {son2} =",son1/son2)



#names = ['Jo\'ravoy', 'Sarvar', 'Ismatilla']
#print(f"Salom {names[2]}, bugun nima qilamiz")
#print(f"{names[0]} qarzini qachon berasan?")

#sonlar = [123, 69, 786, -33, 15.23]
#son_t = (1, 23, 456, 789)
#print(son_t)
#sonlar = sonlar.append(88)
#print(sonlar)
#print(sonlar[0] + sonlar[3])
#print(names[1].title())
#names[2] = 1995
#print(names)
#names[2] = 'Fayzi'
#print(names)
#names.append('Ismat')
#print(names)
#names.insert(2, 'Nursultan')
#print(names)
#names.insert(-1, 'Aziz')
#print(names)
#del names
#print(names)
#names.remove('Aziz')
#print(names)
#print(names.pop())

#t_shaxslar = ['Imom Al-Buxoriy', 'Amir temur', 'Alisher Navoiy']
#z_shaxslar = ['Elon Mask', 'Bill Gates', 'Jeff Bezos', 'Sarvardev']
#print(f"Men tarixiy shaxslardan {t_shaxslar[0]} bilan, zamonaviy shaxslardan {z_shaxslar[0]} bilan suhbatlashgan bo\'lardim")
#print('Men tarixiy shaxslardan', t_shaxslar[0], 'bilan, zamonaviy shaxslardan', z_shaxslar[0], 'bilan suhbatlashgan bo\'lardim')

#bozorlik = ['kartoshka', 'piyoz', 'yog\'', 'pomidor', 'bodring']
#mahsulot = bozorlik.pop(3)
#print('men',mahsulot,'sotib oldim')
#print('endi yana',bozorlik,'larni olishim kerak.')


#nums = list(range(0,10))
#print(nums)
#juft_sons = list(range(2,11,2))
#print(juft_sons)
#toq_sons = list(range(1,10,2))
#print(toq_sons)

#kichj = min(juft_sons)
#kicht = min(toq_sons)
#katj = max(juft_sons)
#katt = max(toq_sons)
#print('kichik sons:',kichj,kicht)
#print('katta sons:',katj,katt)

#cut_nums = nums[:5]
#print(cut_nums)

#newnums = nums[:]
#newnums.append(777)
#print(nums)
#print(newnums)

#countries = ['Uzb','USA','Eng','Rus']
#print(countries)
#print(len(countries))
#print(sorted(countries))
#print(sorted(countries, reverse=True))
#countries.reverse()
#print(countries)
#countries.sort()
#print(countries)
#print(sorted(countries, reverse=True))

#juftlar = list(range(120,1201,2))
#print(juftlar)
#print(sum(juftlar))
#print(max(juftlar)-min(juftlar))
#print(len(juftlar))
#print('boshi:',juftlar[:7])
#print('o\'rtasi:',juftlar[222:232])
#print('oxiri:',juftlar[531:])

#taomlar = ['osh','sho\'rva','manti','kabob','dimlama']
#nonushta = taomlar[:]
#nonushta.remove('sho\'rva')
#nonushta.remove('manti')
#nonushta.remove('kabob')
#nonushta.remove('dimlama')
#nonushta.append('bo\'tqa')
#print(nonushta)
#nonushta = tuple(nonushta)
#nonushta.append('qaymoq')
#print(nonushta)


#sonlar = list(range(11))
#for son in sonlar:
#    print(f'{son} ning kvadrati {son**2} ga teng')

#sonlar = list(range(11))
#son_kvad = []
#for son in sonlar:
#    son_kvad.append(son**2)
#print(sonlar)
#print(son_kvad)
    
#friends = []
#print('eng yaqin 3ta do\'stingiz ismlarini yozing: ')
#for ism in range(3):
#    friends.append(input(f'{ism+1}-do\'stingiz ismini kiriting: '))
#print(friends)



#ismlar = ['Sarvar','Jo\'ravoy','Ismatilla','Aziz','Fayzullo']
#for ism in ismlar:
#print(f'{ism} sen mening eng yaqin do\'stlarimdansan!')
#print(f'Kod {len(ismlar)} marta takrorlandi')


#toq_sons = range(11,100,2)
#for kub in toq_sons:
#    print(f'{kub} ning kubi {kub**3} ga teng.')
    
#kinolar = []
#print('Eng sevimli 5ta filmingizni kiriting: ')
#for kino in range(5):
#    kinolar.append(input(f'{kino+1}-film: '))
#print(kinolar)


#odamlar = int(input('Bugun nechta odam gaplashdingiz?: '))
#ismlar = []
#for ism in range(odamlar):
#    ismlar.append(input(f'{ism+1}-odam: '))
#print(ismlar)


#cars = ['toyota','mazda','hyundai','gm','kia']
#for car in cars:
#    if car == 'gm':
#        print(car.upper())
#    else:
#        print(car.title())


#cars = ['toyota','mazda','hyundai','gm','kia']
#for car in cars:
#    if car != 'gm':
#        print(car.title())
#    else:
#        print(car.upper())

#admin = 'sarvar'
#ism = input('Ismingizni kiriting: ')
#if ism.lower() == admin:
#    print('Xush kelibsiz Admin, foydalanuvchilar ro\'yxatini ko\'rasizmi?')
#else:
#    print(f'Xush kelibsiz {ism.title()}!')

#son1 = int(input('2ta son kiriting\n1-son: '))
#son2 = int(input('2-son: '))
#if son1 == son2:
#    print('Kiritilgan sonlar o\'zaro teng')
#else:
#    print('Sonlar teng emas')


#son = int(input('Istalgan son kiriting: '))
#if son >= 0:
#    print('musbat son')
#else:
#    print('manfiy son')


#son = int(input('Istalgan son kiriting: '))
#if son >= 0:
#    print(son**(1/2))
#else:
#    print('Musbat son kiriting')


#son = int(input("Juft son kiriting:\n"))
#if son % 2 == 0:
#    print('Raxmat!')
#else:
#    print('Bu son juft emas!')
    

#age = int(input("Iltimos, yoshingizni kiriting: "))
#if age <= 4 or age >= 60:
#    narx = 0
#elif age < 18:
#    narx = 10000
#elif age >= 18:
#    narx = 20000
#print(f'sizga kirish narxi {narx} so\'m')
    
#son1 = int(input("1-sonni kiriting: "))
#son2 = int(input("2-sonni kiriting: "))
#if son1 > son2:
#    print(f'{son1}>{son2}')
#elif son1 < son2:
#    print(f'{son1}<{son2}')

#products = ['un','yog\'','shakar','non','guruch','tuz','sabzi','piyoz','kartoshka','pomidor']
#savat = []
#bor_products = []
#mavjud_emas = []
#for n in range(5):
#   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#if savat:
#    for mahsulot in products:
#        if mahsulot in products:
#            bor_products.append(mahsulot)
#        else:
#            mavjud_emas.append(mahsulot)
#    if mahsulot not in mavjud_emas:
#        print(f"Siz so'ragan barcha mahsulot do'konimizda bor")
#    else:
#        print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")       
#else:
#    print("Savatingiz bo'sh")

#users = ['sarvar','jo\'ravoy','ismatilla','fayzullo','aziz']
#new = input("Login kiriting: ")
#if new.lower() in users:
#    print('Login band, yangi login tanlang')
#else:
#    print('Xush kelibsiz!')

#son = int(input('Istalgan butun son kiriting: '))
#for n in range(2,11):
#    if son%n==0:
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
