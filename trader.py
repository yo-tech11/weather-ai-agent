capital = 1000.0

def kelly_criterion(confidence, odds=2.0):
    probability = confidence / 100
    b = odds - 1
    q = 1 - probability

    kelly_fraction = ((b * probability) - q) / b

    return max(0, min(kelly_fraction, 0.25))


def paper_trade(signal, confidence=70):
    global capital

    kelly_fraction = kelly_criterion(confidence)
    stake = round(capital * kelly_fraction, 2)

    if signal == "BUY":
        capital += round(stake * 0.10, 2)

    elif signal == "SELL":
        capital -= round(stake * 0.05, 2)

    return {
        "balance": round(capital, 2),
        "kelly_fraction": round(kelly_fraction, 4),
        "stake": stake,
        "risk_level": (
            "LOW" if kelly_fraction < 0.10
            else "MEDIUM" if kelly_fraction < 0.20
            else "HIGH"
        )
    }