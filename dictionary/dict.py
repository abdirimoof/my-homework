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
davlat = input('Davlatni kiriting: ')
    
#for davlat, info in davlatlar.items():
  
#        print(f'\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}'
#              f'\n Hududi: {info['maydon']} kv.km'
#              f'\n Aholisi: {info['aholi']}'
#              f'\n Pul birligi: {info['pul birligi']}')
   
    
    
        
if davlat in davlatlar.keys():
            info = davlatlar[davlat]
      
            print(f'\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}'
                  f'\n Hududi: {info['maydon']} kv.km'
                  f'\n Aholisi: {info['aholi']}'
                  f'\n Pul birligi: {info['pul birligi']}')
else:
    print('Bunaqa davlat yuq!')
        
        
        
        
        
        
        
        