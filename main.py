# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# constants
HEIGHT = 1.80
WEIGHT = 90
FEET = 10000
TIME = 120

# main.py

Step = (HEIGHT / 4) + 0.37
Length =  FEET * Step
Speed = Length / TIME
Ccal = 0.035 * WEIGHT + (Speed**2 / HEIGHT) * 0.0029 * WEIGHT;

print (f'Расстояние: {Length} , Калории - {Ccal}')
#Расстояние: 181480.0 , Калории - 3319.520561111111
#Расстояние в км: 181.48
KM = Length/1000
print (f'Расстояние в км: {KM}')

if KM > 6:
 print ('Отличная работа!')
elif KM > 4:
 print ('Почти выполнил норму!')
else:
 print ('Давай еще ходи')
