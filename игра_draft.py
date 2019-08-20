###############
print('Start...')
print('~~~игра ПИТОН и другие пш пш ~~~')
name = input('Назовите ваше имя ')
sex = input('Ваш пол M - Ж - Н/о ')
pet_name = input('Назовите имя вашего питомца ')
game_addict_ind = input('Любите ли вы играть? Да/Нет  ')
if game_addict_ind == 'Нет':
   game_addict_ind = 0   
bool_game_addict_ind = bool(game_addict_ind)
print(bool_game_addict_ind)
age = int(input('Сколько вам лет?'))

if age > 90:
    old_bones_ind = input('Это может быть для вас утомительно, вы точно готовы продолжить игру? Да/Нет ')
    if old_bones_ind == 'Да':
        old_bones_ind = input('Вы точно готовы продолжить игру? Да/Нет ')
        if old_bones_ind == 'Да': 
           print('Хорошо',name, ' тогда начнем игру.')  
        else:
            print('Здоровья вам',name, '...')            
    else:
        print('Прощайте',name, '...') 
else:
    if age < 18:
       print('Извините, игра 18+') 
    else:   
       print('Добро пожаловать, ',name)         
#Игра должна сказать: Я могу назвать буквы алфавита, которых нет в твоем имени. и Произнести их. (тут нужен цикл) 
#Пока понимает только нижний регистр :(
namelist = list(name)
alph = 'qwertyuiopasdfghjklzxcvbnm'
i = 0
res = str('')
while i <= len(alph)-1:
    if alph[i] not in namelist:
       res=res+alph[i]    
       i=i+1 
    else:
        i=i+1         
else:
    print('Я могу назвать буквы алфавита, которых нет в твоем имени: ', res)
print('Еnd...')    