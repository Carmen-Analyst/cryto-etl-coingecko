import yfinance as yf

# Función básica
def get_btc_data_range_yf(start_date, end_date):
    btc = yf.Ticker("BTC-USD")
    hist = btc.history(start=start_date, end=end_date)
    return hist

# Prueba 1 rango
if __name__ == "__main__":
    start_date = "2022-11-01"
    end_date = "2023-01-31"

    data = get_btc_data_range_yf(start_date, end_date)

    # Confirma estructura
    print("📊 Head:")
    print(data.head(), "\n")

    # Guarda CSV para ver que no hay fallo de permisos
    data.to_csv("btc_usd_test_nov_jan.csv")
    print("✅ CSV guardado como btc_usd_test_nov_jan.csv")

    # Vuelve a leer para confirmar
    import pandas as pd
    df = pd.read_csv("btc_usd_test_nov_jan.csv", parse_dates=['Date'])
    print("📊 Tail (from CSV):")
    print(df.tail())
