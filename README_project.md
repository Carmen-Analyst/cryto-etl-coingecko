## Análisis comparativo BTC/USD vs BTC/EUR – CoinGecko ETL Project

## Introducción

Bitcoin no es solo una criptomoneda: es un termómetro del sistema financiero moderno. Comprender cómo varía su precio frente al dólar y al euro no es algo reservado a traders profesionales. Es una puerta de entrada para que cualquier persona pueda entender cómo se mueven los mercados, cómo influye la geopolítica en lo digital, y qué señales nos da el comportamiento del dinero en internet.

Este proyecto nace de esa necesidad: hacer accesible un análisis claro y fundamentado sobre el comportamiento de BTC frente a las dos divisas más relevantes para nuestro contexto europeo y global.

## Objetivos

- Extraer y transformar datos horarios de precios BTC/USD y BTC/EUR vía API
- Analizar métricas clave (KPIs) que revelen diferencias de comportamiento
- Identificar oportunidades de arbitraje, momentos de alta volatilidad y señales de tendencia

## KPIs analizados

### 1. Spread medio y desviación estándar
> Diferencia media entre BTC/USD y BTC/EUR a lo largo del tiempo

### 2. Tipo de cambio implícito (EUR/USD derivado de BTC)
> Estimación indirecta del tipo de cambio usando BTC como referencia

### 3.  Volatilidad diaria
> Rango intradía y desviación estándar de ambos pares

### 4. Rendimiento acumulado
> Comparación del crecimiento relativo de BTC/USD y BTC/EUR

### 5. Medias móviles
> Análisis técnico simple mediante MA de 7h y 24h

### 6. Horas con mayor spread
> Identificación de patrones horarios de mayor divergencia

### 7. Outliers
> Detección de valores atípicos que pueden marcar eventos anómalos

## Visualizaciones destacadas

El proyecto incluye más de 10 gráficos generados con `Seaborn` y `Matplotlib`, como:

- Evolución temporal de precios
- Spread y tipo de cambio implícito
- Boxplots por hora
- Volatilidad diaria
- Cruce de medias móviles

## Tecnologías usadas

- Python
- Pandas
- Seaborn / Matplotlib
- Requests
- CoinGecko API
- Git + GitHub

##  Estructura del repositorio
crypto-etl-coingecko/
├── data/
│ └── btc_exchange_rates.csv
├── scripts/
│ ├── etl/
│ │ └── etl_coingecko.py
│ ├── analysis-1-3/
│ │ └── points_1_3.py
│ ├── analysis-4-5/
│ │ └── points_4_5.py
│ ├── analysis-6-7/
│ │ └── points_6_7.py
├── requirements.txt
└── README.md


##  Resultados más llamativos

La diferencia en el rendimiento acumulado entre BTC/USD y BTC/EUR, aunque parezca leve, revela el impacto indirecto del tipo de cambio euro-dólar en la inversión en criptomonedas.

##  Autores

Este proyecto ha sido desarrollado de forma colaborativa por los integrantes del equipo:

- Carmen Fernández
- Luis Rodríguez
- Fernando Botana
- Mónica Cociña

Gracias
