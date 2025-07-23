import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga del CSV
df = pd.read_csv('../../data/btc_exchange_rates.csv', parse_dates=['date'])

# Asegurar orden cronológico
df = df.sort_values('date')

# ========== KPI 1 ==========
# Spread entre BTC/USD y BTC/EUR
df['spread'] = df['price_usd'] - df['price_eur']

# Media y desviación estándar del spread
spread_mean = df['spread'].mean()
spread_std = df['spread'].std()

print(f" Spread medio: {spread_mean:.2f}")
print(f" Desviación estándar del spread: {spread_std:.2f}")

# Línea temporal del spread
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='spread', color='blue')
plt.title('KPI 1: Evolución del Spread BTC/USD - BTC/EUR')
plt.xlabel('Fecha')
plt.ylabel('Spread')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('../../images/kpi1_linea_temporal_spread.png', dpi=300, bbox_inches='tight')


# Boxplot por hora del día
df['hour'] = df['date'].dt.hour
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='hour', y='spread')
plt.title('KPI 1: Distribución del Spread por Hora del Día')
plt.xlabel('Hora')
plt.ylabel('Spread')
plt.tight_layout()
plt.show()
plt.savefig('../../images/kpi1_boxplot_spread_por_hora.png', dpi=300, bbox_inches='tight')

#interpretación kpi 1
print("\n🔎 Interpretación KPI 1:")
print("El spread medio positivo indica que BTC suele tener un valor mayor frente al USD que frente al EUR.")
print("Una desviación estándar de más de 2.000€ sugiere una variabilidad elevada entre ambos mercados.")
print("Este comportamiento puede deberse a factores como la política monetaria de la FED y el BCE,")
print("el volumen de operaciones en exchanges se encuentra dominado por USD, o diferencias horarias de actividad.")


# ========== KPI 2 ==========
# Tipo de cambio implícito EUR/USD usando BTC
df['tipo_cambio'] = df['price_usd'] / df['price_eur']

# Estadísticas
tipo_cambio_mean = df['tipo_cambio'].mean()
tipo_cambio_min = df['tipo_cambio'].min()
tipo_cambio_max = df['tipo_cambio'].max()

print(f"\n Tipo de cambio EUR/USD implícito medio: {tipo_cambio_mean:.4f}")
print(f" Mínimo: {tipo_cambio_min:.4f} |  Máximo: {tipo_cambio_max:.4f}")

# Histograma + KDE
plt.figure(figsize=(12,6))
sns.histplot(df['tipo_cambio'], bins=30, kde=True)
plt.title('KPI 2: Tipo de cambio EUR/USD implícito (BTC/USD ÷ BTC/EUR)')
plt.xlabel('Tipo de cambio implícito')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()
plt.savefig('../../images/kpi2_histograma_tipo_cambio.png', dpi=300, bbox_inches='tight')
# Línea temporal
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='tipo_cambio', color='purple')
plt.title('KPI 2: Evolución temporal del tipo de cambio EUR/USD implícito')
plt.xlabel('Fecha')
plt.ylabel('Tipo de cambio implícito')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('../../images/kpi2_tipo_cambio_eur_usd.png', dpi=300, bbox_inches='tight')

#interpretación del kpi 2


print("\nInterpretación KPI 2:")
print("El tipo de cambio EUR/USD implícito, derivado de los precios de BTC se sitúa en una media de 1.1455.")
print("Este valor es coherente con los niveles históricos reales del par EUR/USD en mercados tradicionales.")
print("La variación entre 1.1079 y 1.1817 indica una cierta dispersión")
print("en la liquidez y el comportamiento de usuarios en exchanges europeos vs estadounidenses.")
print("Comparar este tipo de cambio implícito con el oficial en tiempo real podría revelar oportunidades de arbitraje.")


# ========== KPI 3 ==========
# Añadimos columna con solo la fecha
df['date_only'] = df['date'].dt.date

# Agrupamos por día y calculamos volatilidad
vol = df.groupby('date_only').agg({
    'price_usd': ['max', 'min', 'std'],
    'price_eur': ['max', 'min', 'std']
})

# Renombramos columnas
vol.columns = ['usd_max', 'usd_min', 'usd_std', 'eur_max', 'eur_min', 'eur_std']
vol['vol_usd_range'] = vol['usd_max'] - vol['usd_min']
vol['vol_eur_range'] = vol['eur_max'] - vol['eur_min']

#visualización con print
print("\n Volatilidad diaria (primeras 5 filas):")
print(vol[['vol_usd_range', 'usd_std', 'vol_eur_range', 'eur_std']].head())

#interpretación:

print("\n Interpretación KPI 3:")
print("Se observa una alta volatilidad en BTC/USD y BTC/EUR durante varios días de abril.")
print("El 21 de abril destaca por una volatilidad extrema: más de 3.000 USD de rango intradía.")
print("Esto puede estar vinculado a noticias macroeconómicas, decisiones regulatorias o movimientos institucionales.")
print("Por otro lado, días como el 18 de abril presentan una actividad más contenida.")
print("La volatilidad del par BTC/USD es consistentemente mayor que la del par BTC/EUR,")
print("lo que puede reflejar mayor especulación o volumen de operaciones en mercados en dólares.")
print("Este análisis ayuda a identificar jornadas de riesgo operativo elevado.")

