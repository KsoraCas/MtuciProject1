# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# constants.py
Lab1Height = 180
Lab1Weight = 90
Lab1Feet = 4000
Lab1Time = 120

# main.py

Step = (Lab1Height / 4) + 0.37
Length =  Lab1Feet * Step
Speed = Length / Lab1Time
Ccal = 0.035 * Lab1Weight + ((Speed ** 2) / Lab1Height) * 0.0029 * Lab1Weight;

print (f'Расстояние: {Length} , Калории - {Ccal}')
#Расстояние: 181480.0 , Калории - 3319.520561111111
