import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
 
Data = pd.read_csv(r"Population of India.csv")
Data.head()
df = pd.DataFrame(Data)
 
name = df['State/UT'].head(10)
population = df['Population[50]'].head(10)
male = df['Male'].head(10)
female = df['Female'].head(10)

plt.figure(figsize=(5,5))
plt.bar(name[0:8],population[0:8])
plt.title("Population of States")
plt.xlabel("States")
plt.xticks(rotation=45, ha='right')
plt.ylabel("Population")
plt.show()


barwidth = 0.25
b1 = np.arange(len(male[0:8])) 
b2 = [x + barwidth for x in b1] 
b3 = [x + barwidth for x in b2] 

plt.figure(figsize=(5,5))
plt.bar(b1, male[0:8], color ='r', width = barwidth, 
        edgecolor ='grey', label ='Male') 
plt.bar(b2, female[0:8], color ='g', width = barwidth, 
        edgecolor ='grey', label ='Female') 
plt.title("Population of States")
#plt.xlabel("States")
plt.xticks([a + barwidth for a in range(len(male[0:8]))], 
        ['UP', 'MH', 'BR', 'WB', 'MP','TN','RJ','KA'])
 
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.ylabel("Population")
plt.show()
