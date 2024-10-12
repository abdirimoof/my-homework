#dustim = {'ismi':'jalol', 'tugilgan yili':1998, 'shaxri':'xorazm', 'manzili':'yangibozor'}
#print(f'Dustimning ismi {dustim['ismi'].title()} va tugilgan yili {dustim['tugilgan yili']} \
# va manzili {dustim['shaxri'].title()}' )
 
#dishes = {
##   'vali': 'qosh',
    #'dali': 'bosh',
##   'nali': 'yosh',
  #  'bali': 'shosh'
   # }

#for n,m in dishes.items():
 #   print(f'{m} {n}ning yoqtirgan ovqati')

dictionary = {
    'integer': 'natural son',
    'string': 'matn',
    'float': 'butun son',
    'boolean': 'true va false',
    'if': 'shart sikli',
    'for':'loop',
    'ozgaruvchilar':'malumot qabul qiluvchi'
    }


#check = input('soz kiriting: ')
#for n in dictionary.keys():
#    if n == check:
#        print(dictionary[n])
 
    

#for n,m in sorted(dictionary.items()):
#    print(f'{n} sozining manosi {m}')
 

menu = {
        'osh': 1000,
        'shurva': 2000,
        'jigar': 3000,
        'norin': 4000,
        'shashlik': 5000,
        'baliq': 6000
        } 
book = [] 

#for n in range(1,4):
#    book.append(input(f'{n} - taomni kiriting: '))
#        
 


##for taom in menu.keys():
 #   if taom in book:
  #      print(f'{taom}ning narxi - {menu[taom]}')
        
buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
    "asarlar": [
        "Al-jome’ as-sahih",
        "Al-adab al-mufrad",
        "At-tarix al-kabir",
        "At-tarix as-sag‘ir",
    ],
}

qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent", "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona","asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot", "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],} 


shaxslar = [buxoriy, qodiriy, vohidov,navoiy]
#for n in shaxslar:
#    print(f'{n['ism']} {n['tyil']}-yilda {n['tjoy']}da tavallud topgan. {n['vyil'] - n['tyil']} yil yashagan')
     
#for n in shaxslar:
#    print(f'{n['ism']}ning mashxur asarlari: ')
#    
#    for j in n['asarlar']:
#        print(f'{j} ', end = ' ' )
        
        
        
davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}
#davlat = input('Davlatni kiriting: ')
    
#for davlat, info in davlatlar.items():
  
#        print(f'\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}'
#              f'\n Hududi: {info['maydon']} kv.km'
#              f'\n Aholisi: {info['aholi']}'
#              f'\n Pul birligi: {info['pul birligi']}')
   
    
    
        
#if davlat in davlatlar.keys():
#            info = davlatlar[davlat]
#      
#            print(f'\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}'
#                  f'\n Hududi: {info['maydon']} kv.km'
#                  f'\n Aholisi: {info['aholi']}'
#                  f'\n Pul birligi: {info['pul birligi']}')
#else:
#    print('Bunaqa davlat yuq!')



#print('Sonni kvadratini hisoblash')
##savol = 'sonni kiriting'
#savol += "(agar qiymat 'exit' bulsa dastur tuxtaydi): "
#qiymat = ''
##while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(f'{int(qiymat) ** 2}')
        


#ishora = True

#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
 #       ishora = False
  #  else:
   #     print(f'{int(qiymat) ** 2}')
        
        
        
        
#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(f'{int(qiymat) ** 2}')
 


#print('kitoblar haqida')

#savol = "Yoqtirgan kitobingizni kiriting(agar 'exit' yozsangiz dastur tuxtaydi)"      

#qiymat = ''


#while qiymat.lower() != 'exit':
 #   qiymat = input(savol)
  #  if qiymat != 'exit':
   #     print(f'mening yoqtirgan kitobim {qiymat}')
        
#print('STOP')






#print('chiptaxona')



#savol = 'yoshingizni kiriting agar exit yoki quit yozsangiz dastur tuxtaydi: '

#qiymat = ''

#while (qiymat != 'exit') and (qiymat != 'quit'):
   # qiymat = input(savol)
 #   if (qiymat != 'exit') and (qiymat != 'quit') and (int(qiymat) <= 7):
  #      print('narxi 2000 som')
   # elif (qiymat != 'exit') and (qiymat != 'quit') and (int(qiymat) > 7) and (int(qiymat) <= 18) :
    #    print('Narxi 3000')
#    elif (qiymat != 'exit') and (qiymat != 'quit') and (int(qiymat) > 18) and (int(qiymat) <= 65) :
 #       print('narxi 100001')
  #  elif (qiymat != 'exit') and (qiymat != 'quit') and (int(qiymat) > 65):
   #     print('TEKIN')
#print('dastur tuxtadi')









# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif int(qiymat)<0:
       
#         print(f'{qiymat} musbat son emas!')
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# print('stop')


# savol = 'mahsulotni kiriting agar enough ni kiritsangiz dasrtur tuxtaydi: '
# mahsulotlar = []
# ishora = True
# qiymat = ''
# n = 0


# while ishora:
#     n += 1
    
#     qiymat = (input(f'{n} - {savol}')) 
#     if qiymat == 'enough':
#         break
#     else:    
#         mahsulotlar.append(qiymat)
        
        
# print(mahsulotlar)
    






























# savol = 'mahsulotni kiriting agar enough ni kiritsangiz dasrtur tuxtaydi: '
# savol1 = 'mahsulotni narxini kiriting: '
# mahsulotlar = {}
# ishora= True
# key = ''
# value=0
# n = 0


# while ishora:
#     n += 1
    
#     key = (input(f'{n} - {savol}')) 
    
#     if key == 'enough' :
#         ishora = False
#     else:    
#         value = (int(input(f'{n} - {savol1}')))
#         mahsulotlar[key] = int(value)
        

# for n,m in mahsulotlar.items():
#     print(f'{n}ning  narxi {m} som')

# def age_cal(ismi, yoshi,joriy_yil = 2024):  

    #     """Foydalanuvchini yoshini hisoblovchi funksiya"""
#     print(f'{ismi}nign tugilgan yili - {joriy_yil - yoshi}')




# # age_cal('ali', 27)



# def sq_kub(son):
#     """kub va kvadrat hisoblovchi funksiya"""
#     print(f'{son ** 2} - {son ** 3}')

# # sq_kub(5)
# def qoldiq(son):
#     """qoldiq tekshiradigan funksiya"""
#     for n in range(2,11):
#         if son % n == 0:
#             print(f'{son} {n}ga qoldiqsiz bo`linadi. ')
            
# qoldiq(13)






def malumot(ismi, familiyasi, tugilgan_yi, tugilgan_joyi, email_man = '', telefon_raqami = ''):
    """malumot chiqatuvchi"""
    malumotlar = {
        'ismi': ismi,
        'familiyasi': familiyasi,
        'tugilgan_yil': tugilgan_yi,
        'tugilgan_joy': tugilgan_joyi,
        'email': email_man,
        'telefon_raqam': telefon_raqami
        }
    return malumotlar
    
    # if email_man == False and telefon_raqami == False:
    #     print(ismi,familiyasi,tugilgan_yi,tugilgan_joyi)
    # elif email_man == True and telefon_raqami == False:
    #     print(ismi,familiyasi,tugilgan_yi,tugilgan_joyi,email_man)
    # elif email_man == False and telefon_raqami == True:
    #     print(ismi,familiyasi,tugilgan_yi,tugilgan_joyi,telefon_raqami)
    # else:
    #     print(ismi,familiyasi,tugilgan_yi,tugilgan_joyi,email_man,telefon_raqami)
        




chiqar = malumot("jaxon", "abdirimov", 1998, "xorazm","dfghdfj", "941844214")

print(chiqar)













        




















































        























        
        
        
        
        
        
        
        
        