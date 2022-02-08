# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



H = 180;
W = 90;
F = 4000;
T = 120;

Step = (H / 4) + 0.37
Length =  F * Step
Speed = Length / 120
Ccal = 0.035 * W + ((Speed ** 2) / H) * 0.0029 * W;

print (f'Расстояние: {Length} , Калории - {Ccal}')


