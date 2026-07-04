capital=1000

def paper_trade(signal):

    global capital

    if signal=="BUY":
        capital+=25

    elif signal=="SELL":
        capital-=10

    return capital