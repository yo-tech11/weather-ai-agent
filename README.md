#  Prediction Weather AI Agent

A Python-based Weather AI Agent for internship assessment. The project fetches live weather data, generates weather-based predictions, simulates paper trades, performs Kelly Criterion risk analysis, and displays statistical results through a Streamlit dashboard.

##  Features

- Live weather data
- AI-style weather prediction
- 5-city analysis
- Dehradun support
- Paper trading simulation
- BUY / SELL / HOLD signals
- Kelly Criterion position sizing
- Risk analysis
- Streamlit dashboard
- Statistical results and charts
- Apify integration

##  Supported Cities

- Dehradun
- Mumbai
- London
- Tokyo
- New York

##  Technologies

- Python
- Streamlit
- Pandas
- Requests
- Apify
- Hermes Agent Framework
- Git / GitHub

##  Project Structure

- `main.py` - runs multi-city analysis
- `dashboard.py` - Streamlit user interface
- `weather.py` - weather data fetching
- `predictor.py` - prediction logic
- `trader.py` - paper trading and Kelly risk logic
- `apify_weather.py` - Apify integration
- `outputs/` - sample outputs and statistical results
- `hermes-agent/` - Hermes Agent framework integration

##  Installation

Install dependencies:

```bash
pip install -r requirements.txt