import random as rand



print('1 dan 10 gacha son uyladim topa olasizmi. \n')
#my_number = int(input('Agar uylagan bulsangiz sonni kiriting: '))



def son_top(x = 10):
    camp_number = rand.randint(1, x)
    n = 0
    print('Agar uylagan bulsangiz sonni kiriting: ')
    while True:
        my_number = int(input('>>>>'))
        n += 1;
        if((my_number < camp_number)):
            print('men uylagan son kattoroq: ')
            
        elif((my_number > camp_number)):
          print('Men uylagan son kichikroq: ')
        else:
            break
    print(f'siz {n} ta urinishda topdingiz')
           
    
    return n 




def son_top_pc(x = 10):
    taxmin = 0
    n_1 = 0
    quyi = 1
    yuqori = x
    while True:
        n_1 += 1
        taxmin = rand.randint(quyi, yuqori)
        javob = input(f'Siz {taxmin} sonini uyladingiz .t + -')
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f'Men {n_1} ta taxmin bn topdinm')
        
    return n_1



def play(x = 10):
    yana = True
    
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)
        
        if taxminlar_pc > taxminlar_user:
            print("Siz yutdingiz")
        elif taxminlar_pc < taxminlar_user:
            print('men yutdim')
        else:
            print('DURRANG')
        yana = int(input(f'yana uynaysizmi ha(1), yuq(0)'))
    
        
    
uyin = play(x=10)



