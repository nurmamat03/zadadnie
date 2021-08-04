dates_of_birth = {3,10,7,13,31,7,1,10,7,5,6,6}
dates_of_birth.remove(7)
print(dates_of_birth)


farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
a=farm_1.intersection(farm_2)
print(a)

farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_1.difference(farm_2)
print(farm_1)

i = {23,24,55,66,5}
i.add(7)
i.pop()
print(i)

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
b = {'bech_barmak': 130}
menu.update(b)
print(menu)
menu['lagman']=135
print(menu)
menu.pop('borsh')
print(menu)

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks']=['Coca-Cola', 'Sprite', 'Fanta']
print(menu)

a = {'.add','.update', '.intersection','.remove','.clear','.update','.difference','.discard','.intersection','.intersection_update','.pop'}
b = {'.clear', '.get','.values','.update'}
c = a.intersection(b)
print(c)

l = {}
for i in range(3):
    a = input('Введите имя :')

for i in range(3):
    b =  int(input('Введите пaроль : '))
l[a]=b
print(l)

a = {'Azat': 'mentor' , 'Айдар' : 'Мерчендайзер', "Улан": "Астронафт" , "Нурайым":"Бухгалтер" , "Баэл":"Таксист" }
for i , y in a.items():
    print("Здраствуйте", i ,"Прекрастная профессия" ,y )

a = set()
for x in range(10):
    p = input("Введите номер : ")
    a.add(p)
print(a)

south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',    'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a = {}
a=set(south_american_countries)
print(list(a))
'''


