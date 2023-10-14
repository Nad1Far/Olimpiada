a = int(input()) #Очки Алисы
b = int(input()) #Очки Боба

Wb = 0 #Победы Боба
Wa = 0 #Победы Алисы
Draw = 0 #Ничьи
Fb = 0 #Проигрыши Боба
Fa = 0 #Проигрыши Алисы

while a != 0 and b != 0:
    a -= 1
    b -= 1
    Draw += 1
    
    
print(a, b, Draw)
