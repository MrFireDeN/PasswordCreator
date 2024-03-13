import math

L = 1
alphabet=[10, 22, 26, 33, 36, 43, 48, 55, 58, 62, 66, 74, 76, 84, 88, 98]# длинна алфавитов

# Задание 1.1
def passCalc(V,T,P): #нижняя граница S*
    return math.ceil(math.fabs((V*T)/P))

# Задание 1.2
def printA(alphabet, L):
    for A in alphabet:
        while passCalc(15*60*24, 20, 10**-7)>=A**L:
            L+=1
        print(f"A = {A}\tL = {L}")
        L=1

# Задание 2
def passwords(A,L,V,m,v):
    S=A**L
    T=S/V

    Ti=T+((T*v)/m)
    Ti= Ti/(60*60*24)
    return Ti

# Задание 3
def passMin(A,T,V):
    S=T*V*365*24*60*60
    L= math.ceil(math.log(S,A))
    return L

print(f"Задание 1.1\nS* = {passCalc(15*60*24, 20, 10**-7)}")

print(f"Задание 1.2")
printA(alphabet, L)

print(f"Задание 2\nНа взлом нужно {passwords(150, 3, 200, 5, 3)} дней")

print(f"Задание 3\nМинимальная длина пароля: {passMin(150, 30, 200)}")