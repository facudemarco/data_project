import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ec_sales.csv')

df['date'] = pd.to_datetime(df['date'])

print(df.head())

plt.figure(figsize=(12,6))
plt.plot(df['date'], df['value'], marker='o', color='blue')
plt.title('Evolución de Ventas de E-commerce por Trimestre (EE.UU.)')
plt.xlabel('Año')
plt.ylabel('Ventas (en millones USD)')
plt.grid(True)
plt.tight_layout()
plt.show()