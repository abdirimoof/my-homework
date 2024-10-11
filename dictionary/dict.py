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

for n in range(1,4):
    book.append(input(f'{n} - taomni kiriting: '))
        
 


for taom in menu.keys():
    if taom in book:
        print(f'{taom}ning narxi - {menu[taom]}')
    
        
        
        
        
        
        
        
        
        
        
        