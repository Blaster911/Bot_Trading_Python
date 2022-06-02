price = 26000
buy = 25000
pourcentage = 2
calcBuyUp = buy + (buy * pourcentage / 100)
calcBuyDown = buy - (buy * pourcentage / 100)

if(price > buy):
    print("achat en cours...")