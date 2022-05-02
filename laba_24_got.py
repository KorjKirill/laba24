'''
Сортировка по дате и выведение данных
'''
import matplotlib.pyplot as plt
import pandas as pd
f1 = pd.read_csv("TED Talks.csv")
df1 = pd.DataFrame(f1)

df2 = df1.sort_values(by="date")
plt.bar(df2['date'],df2['views'])
plt.show()
print(df2)
print()
plt.bar(df2['date'],df2['likes'])
plt.show()
print(df2)
print()
