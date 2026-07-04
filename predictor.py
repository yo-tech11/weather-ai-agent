def predict(weather):

    current=weather["current_condition"][0]

    temp=int(current["temp_C"])
    humidity=int(current["humidity"])

    if humidity>80:
        prediction="Rain"
        confidence=90
        trade="BUY"

    elif humidity>60:
        prediction="Maybe Rain"
        confidence=70
        trade="HOLD"

    else:
        prediction="No Rain"
        confidence=55
        trade="SELL"

    return{
        "temperature":temp,
        "humidity":humidity,
        "prediction":prediction,
        "confidence":confidence,
        "trade":trade
    }