# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# constants
HEIGHT = 1.80
WEIGHT = 90
FEET = 10000
TIME = 120

# main.py

step = (HEIGHT / 4) + 0.37
length =  FEET * step
speed = length / TIME
ccal = 0.035 * WEIGHT + (speed**2 / HEIGHT) * 0.0029 * WEIGHT;

print (f'Расстояние: {length} , Калории - {ccal}')
#Расстояние: 181480.0 , Калории - 3319.520561111111
#Расстояние в км: 181.48
kilometers = length/1000
print (f'Расстояние в км: {kilometers}')

if kilometers > 6:
 print ('Отличная работа!')
elif kilometers > 4:
 print ('Почти выполнил норму!')
else:
 print ('Давай еще ходи')
