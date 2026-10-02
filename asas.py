import random 
import matplotlib.pyplot as plt 
plt.figure(figsize=(14, 9))
shag = 0
cnt = 0
s1 = []
cnt1 = []
for i in range(1,1001):
    choice = [-1,1]
    shag+=random.choice(choice)
    cnt+=1
    s1.append(shag)
    cnt1.append(cnt)
    print(shag)
plt.subplot(1, 2, 1)
plt.scatter(s1, cnt1, color="blue")
plt.subplot(1, 2, 2)
plt.hist(s1,bins = 100)
plt.show()