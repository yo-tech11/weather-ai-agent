from weather import get_weather
from predictor import predict
from trader import paper_trade

cities=[
"Delhi",
"Mumbai",
"London",
"Tokyo",
"New York"
]

for city in cities:

    weather=get_weather(city)

    result=predict(weather)

    balance=paper_trade(result["trade"])

    print("="*60)
    print(city)
    print(result)
    print("Balance :",balance)