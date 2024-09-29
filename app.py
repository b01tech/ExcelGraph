import pandas as pd
import matplotlib.pyplot as plt

var path = 'arquivo.xlsx'
df = pd.read_excel(path, engine='openpyxl')

print(df.head())

plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Values'])


plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Graphic')

plt.show()
