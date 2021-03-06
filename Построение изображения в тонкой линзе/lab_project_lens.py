# Лабораторная работа №6. Задание 3
import numpy as np
import matplotlib.pyplot as plt

# ----------------- МОЖНО ИССЛЕДОВАТЬ ПАРАМЕТРЫ: ---------------------------
F = 10 #фокусное расстояние
d = 25 #расстояние предмета от линзы
type = 0 #тип линзы: 0 - собирающая линза, 1 - рассеивающая линза
h = 10 #высота предмета
Height = 20 #высота линзы (рассмотрен простой случай - высота линзы больше высоты предмета)
# ---------------------------------------------------------------------

#создание пустых массивов
OsX=[]
OsY=[]
PredmetX=[]
PredmetY=[]
LensX=[]
LensY=[]

if type == 0:
    f = 1 / (1 / F - 1 / d) #расчет по формуле тонкой линзы расстояния от линзы до изображения

for i in range(100):
    OsX.append(-d+(f+d)*i/100) #массив x-координат оптической оси (рисуем от предмета до изображения)
    OsY.append(0) #массив y-координат оптической оси
    PredmetX.append(-d) #массa х-координат предмета, находящегося слева от линзы
    PredmetY.append(0+h*i/100) #массив y-координат предмета
    LensX.append(0) #массив x-координат линзы (она находится в точке x=0)
    LensY.append(-Height+2*Height*i/100) #массив y-координат линзы (от -Height до Height)

k = - h / d #угловой коэффициент прямой, по которой идет луч, проходящий через оптический центр
r = - h / F #угловой коэффициент прямой, по которой идет луч после преломления

LX=[]
L1Y=[]
L2Y=[]

for i in range(100):
    x=-d+d*i/100 #перебор x-координат перед линзой
    LX.append(x) #заполнение массива x-коордлинат для лучей
    L1Y.append(h)#массив y-координат луча, идущего параллельно оптической оси
    L2Y.append(k*(x+d)+h) #массив y-координат луча, идущего через центр линзы

LX_2 = []
L1Y_2 = []
L2Y_2 = []

for i in range(100):
    x=0+f*i/100 #перебор х-координат после линзы
    LX_2.append(x) #заполнение массива x-координат для лучей после линзы
    L1Y_2.append(r*x+h) #массив y-координат луча, преломленного линзой
    L2Y_2.append(k*x) ##массив y-координат луча, идущего через центр линзы

H = k * f #высота изображения

ImageX = []
ImageY = []

for i in range(100):#массивы координат для изображения
    ImageX.append(f)
    ImageY.append(H*i/100)

#рисование всего на одном графике
fig = plt.figure(facecolor='white')
plt.plot(PredmetX,PredmetY,color='b',linewidth=5)
plt.plot(OsX,OsY,'--',linewidth=4,color='g')
plt.plot(ImageX,ImageY,color='b',linewidth=5)
plt.plot(LensX,LensY,'--',linewidth=4,color='g')
plt.plot(LX,L1Y,'--',color='y')
plt.plot(LX,L2Y,'--',color='y')
plt.plot(LX_2,L1Y_2,'--',color='y')
plt.plot(LX_2,L2Y_2,'--',color='y')
plt.ylabel("x")
plt.xlabel("y")
plt.grid(True)
plt.show()
