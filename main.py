from weather import get_weather
from predictor import predict
from trader import paper_trade
cities = [
    "Dehradun",
    "Mumbai",
    "London",
    "Tokyo",
    "New York"
]
print("\n" + "=" * 65)
print(" WEATHER AI AGENT")
print("Weather Prediction & Paper Trading System")
print("=" * 65)


for city in cities:

    try:

        print("\n" + "=" * 65)
        print(f" City: {city}")
        print("=" * 65)

        # Fetch live weather data
        weather = get_weather(city)

        if weather is None:
            print(
                f" Weather data could not be fetched for {city}"
            )
            continue


        result = predict(weather)


        trade_result = paper_trade(
            result["trade"],
            result["confidence"]
        )

        print("\n LIVE WEATHER DATA")

        print(
            " Temperature:",
            result["temperature"],
            "°C"
        )

        print(
            " Humidity:",
            result["humidity"],
            "%"
        )

        print("\n PREDICTION RESULT")

        print(
            "Prediction:",
            result["prediction"]
        )

        print(
            "Confidence:",
            f'{result["confidence"]}%'
        )

        print(
            "Trade Signal:",
            result["trade"]
        )

        print("\n PAPER TRADE ORDER")

        if result["trade"] == "BUY":

            print(
                "BUY order simulated successfully"
            )

        elif result["trade"] == "SELL":

            print(
                " SELL order simulated successfully"
            )

        else:

            print(
                "⏸ HOLD — No new position opened"
            )

        print("\n KELLY CRITERION RISK ANALYSIS")

        print(
            "Paper Balance:",
            f'₹{trade_result["balance"]:.2f}'
        )

        print(
            "Kelly Stake:",
            f'₹{trade_result["stake"]:.2f}'
        )

        print(
            "Kelly Fraction:",
            f'{trade_result["kelly_fraction"]:.4f}'
        )

        print(
            "Risk Level:",
            trade_result["risk_level"]
        )


    except Exception as e:

        print(
            f"\n Error processing {city}: {e}"
        )

print("\n" + "=" * 65)
print(" Analysis completed for all supported cities")
print("=" * 65)

print(
    "\n Educational project — "
    "simulated paper trading only."
)

print(
    "No real-money trades are executed.\n"
)