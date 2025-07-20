import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#leer el csv y calcular el spread para el punto 6
df = pd.read_csv('../../data/btc_exchange_rates.csv', parse_dates=['date'])

df ['spread'] = abs(df['price_usd']- df['price_eur'])

#extrayendo la hora del día
df['hour'] = df['date'].dt.hour

#agrupando por hora y calcular la media ponderada (promedio) del spread:
spread_by_hour =df.groupby(['hour'])['spread'].mean()

#calculando los kpi que son el máximo y mínimo por hora:
hora_mayor_spread =spread_by_hour.idxmax()
hora_menor_spread = spread_by_hour.idxmin()

#visualizando:
print(f"hora con mayor spread promedio: {hora_mayor_spread}h - Spread: {spread_by_hour.idxmax(): .2f}")
print(f"hora con menor spread promedio: {hora_menor_spread}h - Spread: {spread_by_hour.idxmin(): .2f}")

#visualización
# Reiniciamos el índice para que 'hour' sea una columna
spread_df = spread_by_hour.reset_index()

# Ordenamos por spread descendente para ver claramente los picos
spread_df_sorted = spread_df.sort_values(by='spread', ascending=False)

plt.figure(figsize=(12, 6))
ax = sns.barplot(x='hour', y='spread', data=spread_df_sorted, palette='crest')

plt.title('Spread promedio BTC/USD - BTC/EUR por hora del día', fontsize=14)
plt.xlabel('Hora del día')
plt.ylabel('Spread promedio')
plt.xticks(rotation=45)

# Añadimos valores encima de las barras
for i, row in spread_df_sorted.iterrows():
    ax.text(i, row['spread'] + 0.5, f"{row['spread']:.2f}", ha='center', va='bottom', fontsize=8)

# Rango Y ajustado
plt.ylim(spread_df['spread'].min() - 2, spread_df['spread'].max() + 5)

plt.tight_layout()
plt.show()


interpretacion = """
INTERPRETACIÓN PROFESIONAL DEL SPREAD HORARIO


Hora con mayor spread promedio: 09:00 (13,260.08)
Hora con menor spread promedio: 17:00 (13,155.49)

Análisis:
- El mayor spread ocurre en la apertura de mercados europeos, con volatilidad alta.
- El menor spread coincide con el solapamiento EU/US, lo que implica mayor liquidez.

Recomendación:
- Operar entre 16h-18h si se busca minimizar costes de spread.
- Explorar patrones similares en otros pares o criptomonedas.
"""

print(interpretacion)



#punto 7 la detección de outliers con la media y la desviación típica o estándar:
# Calcular la media y desviación estándar
mean_spread = df['spread'].mean()
std_spread = df['spread'].std()

# Filtrar outliers moderados y fuertes: 2 desviaciones es moderado, 3 es fuerte
outliers_2std = df[(df['spread'] > mean_spread + 2*std_spread) | (df['spread'] < mean_spread - 2*std_spread)]
outliers_3std = df[(df['spread'] > mean_spread + 3*std_spread) | (df['spread'] < mean_spread - 3*std_spread)]

# KPIs y visualización de resultados
print(f"Número de outliers fuera de 2 desviaciones estándar: {len(outliers_2std)}")
print(f"Número de outliers fuera de 3 desviaciones estándar: {len(outliers_3std)}")

#gráficos: histograma con líneas de corte por desviación típica o estándar:

plt.figure(figsize=(10, 5))
sns.histplot(df['spread'], kde=True, bins=30, color='skyblue')
plt.axvline(df['spread'].mean(), color='green', label='Media', linestyle='-')
plt.axvline(df['spread'].mean() + 2*df['spread'].std(), color='red', linestyle='--', label='+2σ')
plt.axvline(df['spread'].mean() - 2*df['spread'].std(), color='red', linestyle='--', label='-2σ')
plt.title('Distribución del spread y detección de outliers')
plt.xlabel('Spread')
plt.ylabel('Frecuencia')
plt.legend()
plt.tight_layout()
plt.show()

#interpretación de resultados del punto 7

print("7. Análisis de Outliers en el Spread BTC/USD vs BTC/EUR\n")
print("Se ha analizado la distribución del spread horario entre BTC/USD y BTC/EUR para detectar comportamientos anómalos.\n")
print("- ±2σ (2 desviaciones estándar): Se han detectado 12 outliers moderados.")
print("- ±3σ (3 desviaciones estándar): No se han encontrado valores fuera de este rango.\n")
print("Interpretación:")
print("Aunque no se detectan eventos extremos, los valores fuera de ±2σ presentan un grado de desviación claramente acusado respecto a la media.")
print("Estas anomalías pueden deberse a eventos puntuales de volatilidad, desfase entre plataformas de intercambio o efectos de apertura/cierre de mercados internacionales.\n")
print("Recomendación:")
print("Si se usa el spread como variable para modelos, se recomienda suavizar el efecto de los outliers, por ejemplo, limitando sus valores extremos ('winsorizing').")
print("Alternativamente, investigar en detalle los días con outliers para identificar causas específicas.")



