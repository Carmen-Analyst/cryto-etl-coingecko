# -----------------------------
# KPI 4: Rendimiento Acumulado
# KPI 5: Medias Móviles
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga tu dataset (ajusta ruta si es necesario)
df = pd.read_csv('../../data/btc_exchange_rates.csv', parse_dates=['date'])


# Aseguramos orden cronológico
df = df.sort_values('date')

# ===================================================
# KPI 4: Rendimiento acumulado BTC/USD y BTC/EUR
# ===================================================

# Cálculo del cambio porcentual y rendimiento acumulado
df['return_usd'] = df['price_usd'].pct_change()
df['return_eur'] = df['price_eur'].pct_change()

df['cum_return_usd'] = (1 + df['return_usd']).cumprod()
df['cum_return_eur'] = (1 + df['return_eur']).cumprod()

# Gráfico de rendimiento acumulado
plt.figure(figsize=(12,6))
sns.lineplot(x='date', y='cum_return_usd', data=df, label='BTC/USD')
sns.lineplot(x='date', y='cum_return_eur', data=df, label='BTC/EUR')
plt.title('KPI 4: Rendimiento acumulado de BTC/USD vs BTC/EUR')
plt.xlabel('Fecha')
plt.ylabel('Rendimiento acumulado')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Interpretación
print("🔎 Interpretación KPI 4:")
print("Este gráfico permite ver la rentabilidad acumulada de cada tipo de cambio.")
print("Una pendiente más pronunciada indica mayor crecimiento relativo.")
print("Divergencias entre BTC/USD y BTC/EUR pueden revelar oportunidades o brechas.")

# ===================================================
# KPI 5: Medias móviles (7h y 24h)
# ===================================================

# Cálculo de medias móviles
df['ma_7h_usd'] = df['price_usd'].rolling(window=7).mean()
df['ma_24h_usd'] = df['price_usd'].rolling(window=24).mean()
df['ma_7h_eur'] = df['price_eur'].rolling(window=7).mean()
df['ma_24h_eur'] = df['price_eur'].rolling(window=24).mean()

# Gráfico para BTC/USD
plt.figure(figsize=(12,6))
sns.lineplot(x='date', y='price_usd', data=df, label='BTC/USD', alpha=0.3)
sns.lineplot(x='date', y='ma_7h_usd', data=df, label='MA 7h BTC/USD')
sns.lineplot(x='date', y='ma_24h_usd', data=df, label='MA 24h BTC/USD')
plt.title('KPI 5: Medias móviles BTC/USD')
plt.xlabel('Fecha')
plt.ylabel('Precio BTC/USD')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico para BTC/EUR
plt.figure(figsize=(12,6))
sns.lineplot(x='date', y='price_eur', data=df, label='BTC/EUR', alpha=0.3)
sns.lineplot(x='date', y='ma_7h_eur', data=df, label='MA 7h BTC/EUR')
sns.lineplot(x='date', y='ma_24h_eur', data=df, label='MA 24h BTC/EUR')
plt.title('KPI 5: Medias móviles BTC/EUR')
plt.xlabel('Fecha')
plt.ylabel('Precio BTC/EUR')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Interpretación4
print("🔎 Interpretación KPI 4:")
print("Durante el período observado (abril–julio 2025), tanto BTC/USD como BTC/EUR han mostrado un crecimiento acumulado similar,")
print("aunque BTC/USD ha tenido repuntes más pronunciados en ciertos momentos, especialmente a finales de junio y mediados de julio.")
print("Esto sugiere que el dólar ha estado más expuesto a movimientos de impulso en el mercado cripto.")
print("Por otro lado, BTC/EUR mantiene un comportamiento más estable, con menor amplitud en los picos.")
print("La divergencia a partir de julio puede estar relacionada con factores macroeconómicos o de política monetaria entre EE. UU. y Europa.")
#interpretación del punto 5
print("🔎 Interpretación KPI 5:")
print("Las medias móviles de 7h y 24h para BTC/USD muestran una clara tendencia alcista, con múltiples puntos de cruce entre ambas.")
print("A partir de mayo, la MA de 7h cruza repetidamente por encima de la de 24h, lo que puede interpretarse como señales de entrada (momentum positivo).")
print("En las semanas previas al 15 de julio, el cruce sostenido hacia arriba confirma una fase expansiva del precio.")
print("No se observan cruces bajistas duraderos.")
print("Este patrón sería interesante para modelos de predicción basados en señales técnicas simples.")
