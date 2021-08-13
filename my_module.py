'''
print ("Я функция из my_module.py")
import sys
print(sys.platform)

import random
b = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
m=random.sample(b,4)
print(m)

from random import sample
b = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai"]
print(sample(b,2))

import sys
print(sys.platform)

from math import pi
print(pi)
'''
import sys
print("Привет {}. Добро пожаловать в руководство по {} на {}".format(sys.argv[1],sys.argv[2],sys.argv[3]))
'''
import os
import random
os.mkdir("range")
for i in range(5):
  os.mkdir(f'/home/nuru/lesson/range/1{random.randint(1,33)}.txt')

k1 = []
k2 = []
k3 = []
k4 = []
i = 0
while i < 3:
  q = choice(names)
  if q not in k1:
    k1.append(q)
    i+=1
i = 0
while i < 3:
  f = choice(names)
  if f not in k1 and f not in k2:
    k2.append(f)
    i+=1
i = 0
while i < 3:
  q = choice(names)
  if q not in k1 and q not in k2 and q not in k3:
    k3.append(q)
    i+=1
i = 0
while i < 3:
  f = choice(names)
  if f not in k1 and f not in k2 and f not in k3 and f not in k4:
    k4.append(f)
    i+=1
print("Команда 1",k1)
print("Команда 2",k2)
print("Команда 3",k3)
print("Команда 4",k4)
'''
