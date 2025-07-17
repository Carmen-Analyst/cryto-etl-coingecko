import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_btc_data(vs_currency='usd', days=90):
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', f'price_{vs_currency}'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['date', f'price_{vs_currency}']]
    return df

btc_usd = get_btc_data('usd')
btc_eur = get_btc_data('eur')

btc_data = pd.merge(btc_usd, btc_eur, on='date')

btc_data.to_csv('data/btc_exchange_rates.csv', index=False)
print("✅ Archivo guardado: data/btc_exchange_rates.csv")

plt.figure(figsize=(12, 6))
plt.plot(btc_data['date'], btc_data['price_usd'], label='BTC/USD')
plt.plot(btc_data['date'], btc_data['price_eur'], label='BTC/EUR')
plt.title('Bitcoin Exchange Rates (Últimos 90 días)')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.legend()
plt.show()



import pandas as pd

# Ruta al archivo generado por tu ETL
df = pd.read_csv('data/btc_exchange_rates.csv', parse_dates=['date'])

# Muestra las primeras filas
print(df.head())

# Muestra info básica: columnas, tipos, nulos
print("\n📊 Info general:")
print(df.info())

# Estadísticas básicas
print("\n📈 Estadísticas descriptivas:")
print(df.describe())
