import random 
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))
shag = 0
cnt = 0
s1 = []
cnt1 = []
choice = [-1,1]
for i in range(1,1001):
    shag+=random.choice(choice)
    cnt+=1
    s1.append(shag)
    cnt1.append(cnt)
pozition = []
sumkvadr = [0] * 1001
for i in range(1000):
    chast = 0
    for j in range(1, 1001):
        chast += random.choice(choice)
        sumkvadr[j] += chast**2
    pozition.append(chast)
otkl = []
for i in range(1001):
    a = sumkvadr[i] / 1000
    otkl.append(a**0.5)

plt.subplot(1, 3, 1)
plt.plot(cnt1,s1, color="blue")
plt.xlabel('Шаги')
plt.ylabel('Положение')

plt.subplot(1, 3, 2)
plt.hist(pozition,bins = 25,edgecolor="black")
plt.xlabel("Конечная координата")
plt.ylabel("Количество частиц")

plt.subplot(1, 3, 3)
plt.plot(otkl, color="orange", label="Экспериментальный")
theor = [n**0.5 for n in range(1001)]
plt.plot(theor, color="black", linestyle="--", label="Теоретический")
plt.xlabel("Шаги")
plt.ylabel("Отклонение")
plt.legend()
plt.show()