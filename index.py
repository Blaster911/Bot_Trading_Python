# # phase TEST
from trade import Trade
from utils import *


# Variables
nameFileConfig = "myWallet.ini"
nameParam = 'WALLET'
percentBuySell = 1
addSection = {nameParam: {'BTC': '1',
                          'BUSD': '28000'},
              }
BUSD_price = float(1)

# calcule la différence entre deux valeurs
def calc(nbrInf, nbrSupr):
    volume = nbrSupr - nbrInf
    return volume/2

# Calcule la quantité à acheter ou vendre
def quantityTrade(result, priceToken):
    return result / priceToken

def choiceBuySell(nbr1, nbr2):
    nbr2 = int(nbr2)
    nbr1 = int(nbr1)
    state = None
    # Bearish
    log(str(nbr1) + " " + str(nbr2) )
    if(nbr1 < nbr2):
        result = calc(nbr1, nbr2)
        state = "Bear"   
    # Bullish
    if(nbr2 < nbr1):
        result = calc(nbr2, nbr1)
        state = "Bull"
    # ecart Null
    elif (nbr2 == nbr1):
        result = 0
        state = None
    return result, state

# def comparePercent(nbr1, nbr2):

while True:
    config = openOrCreateFile(nameFileConfig, "config", addSection)
    BTC_price = float(input("Indiquer le prix du bitcoin : "))
    quantity_BTC = float(config['WALLET']["BTC"])
    quantity_BUSD = float(config['WALLET']["BUSD"])
    value_BTC = BTC_price * quantity_BTC
    value_BUSD = BUSD_price * quantity_BUSD


    result = choiceBuySell(value_BTC, value_BUSD)
    priceGap = result[0]
    bearOrBull = result[1]

    quantity = quantityTrade(priceGap, BTC_price)

    if(bearOrBull == "Bull"):
        valueToken = round(quantity_BTC - quantity, 2)
        log("Quantité vendu : " + str(round(-quantity, 2)))
        log("Quantité Total : " + str(valueToken))
        rewriteSection = {nameParam: {'BTC': valueToken,
                        'BUSD': '28000'},
        }
        rewriteFile(nameFileConfig, rewriteSection)
    if(bearOrBull == "Bear"):
        valueToken = round(quantity_BTC + quantity, 2)
        log(quantity_BTC)
        log("Quantité acheter : " + str(round(quantity, 2)))
        log("Quantité Total : " + str(valueToken))
        rewriteSection = {nameParam: {'BTC': valueToken,
                'BUSD': '28000'},
        }
        rewriteFile(nameFileConfig, rewriteSection)

    log("Ecart de prix : " + str(priceGap) + " Etat : " + str(bearOrBull))










# ----------- Element rentrant ->
# priceUSDT = 1
# priceBTC = 25000
# priceETH = 2000

# # -- My wallet ->
# quantity_BTC = 0.05
# quantity_ETH = 0.5
# quantity_USDT = 2400
# valueAll = quantity_ETH * priceETH + quantity_BTC * priceBTC + quantity_USDT * priceUSDT
# valueETH = (quantity_ETH * priceETH)
# valueBTC = (quantity_BTC * priceBTC)
# print(valueAll)

# # Trading Active => ETH 
# pourcentagePriceEcart = 2
# pourcentageBuy = 2

# # quantityBuy = 30
# # quantityToken = quantityBuy/priceToken
# # print(quantityToken)

# while True:
#     price = input("Rentrer le prix du token :")
#     calcBuyUp = buy + (buy * pourcentagePriceEcart / 100)
#     calcBuyDown = buy - (buy * pourcentagePriceEcart / 100)

#     if(float(price) <= calcBuyUp):
#         print("non. prix d'achat minimum : " + str(calcBuyUp))
#     if(float(price) > calcBuyUp):
#         print("Achat en cours...")
#         priceBuy = float(price)
#         print(priceBuy)
#         moy = (priceBuy + buy)/2
#         # quantityToken = quantityBuy/priceBuy
#         print("quantité acheter : ")
#         print("Acheter à : " + str(moy))