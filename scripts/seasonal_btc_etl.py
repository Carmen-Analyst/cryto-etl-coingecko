# scripts/seasonal_btc_etl.py

import requests
import pandas as pd
import datetime
import os
import json

def get_btc_data_range(vs_currency, from_timestamp, to_timestamp):
    """
    Llama al endpoint CoinGecko market_chart/range y devuelve los datos JSON.
    """
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range'
    params = {
        'vs_currency': vs_currency,
        'from': from_timestamp,
        'to': to_timestamp
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Lanza error si hay problema con la petición
    return response.json()

# Definir periodos estacionales donde puede haber más variabilidad
periods = [
    {'name': 'nov_jan', 'start': (11, 1), 'end': (1, 31)},
    {'name': 'mar_may', 'start': (3, 1), 'end': (5, 31)},
    {'name': 'jul_sep', 'start': (7, 1), 'end': (9, 30)}
]

# Años a comparar: los últimos 3 períodos
years = [2022, 2023, 2024]

# Monedas con las que comparamos
vs_currencies = ['usd', 'eur']

# Crear carpetas si no existen
os.makedirs('raw_data', exist_ok=True)
os.makedirs('data', exist_ok=True)

for year in years:
    for period in periods:
        for currency in vs_currencies:

            # Ajustar año de inicio y fin (si el periodo cruza año)
            start_year = year
            end_year = year if period['start'][0] < period['end'][0] else year + 1

            start_date = datetime.datetime(start_year, period['start'][0], period['start'][1])
            end_date = datetime.datetime(end_year, period['end'][0], period['end'][1])

            from_ts = int(start_date.timestamp())
            to_ts = int(end_date.timestamp())

            print(f"🔍 Fetching BTC/{currency.upper()} | {period['name']} | {start_date.date()} - {end_date.date()}")

            # Obtener datos
            data = get_btc_data_range(currency, from_ts, to_ts)

            # Guardar JSON crudo
            raw_filename = f"raw_data/btc_{currency}_{period['name']}_{year}.json"
            with open(raw_filename, 'w') as f:
                json.dump(data, f)
            print(f"✅ JSON guardado: {raw_filename}")

            # Transformar a DataFrame
            prices = data.get('prices', [])
            if not prices:
                print(f"⚠️ No se encontraron precios para {currency} {period['name']} {year}")
                continue

            df = pd.DataFrame(prices, columns=['timestamp', f'price_{currency}'])
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df = df[['date', f'price_{currency}']]

            # Guardar CSV limpio
            clean_filename = f"data/btc_{currency}_{period['name']}_{year}.csv"
            df.to_csv(clean_filename, index=False)
            print(f"✅ CSV guardado: {clean_filename}")

print("Proceso ETL estacional terminado.")





# seasonal_btc_etl_yfinance.py

import yfinance as yf

def get_btc_data_range_yf(start_date, end_date):
    btc = yf.Ticker("BTC-USD")
    hist = btc.history(start=start_date, end=end_date)
    return hist

seasons = {
    "nov_jan_2022": ("2022-11-01", "2023-01-31"),
    "mar_may_2022": ("2022-03-01", "2022-05-31"),
    "jul_sep_2022": ("2022-07-01", "2022-09-30")
}

for season_name, (start, end) in seasons.items():
    print(f"🔍 Fetching BTC/USD | {season_name} | {start} - {end}")
    data = get_btc_data_range_yf(start, end)
    csv_filename = f"btc_usd_{season_name}.csv"
    data.to_csv(csv_filename)
    print(f"✅ Saved {csv_filename}")
    print(data.head(), "\n")
