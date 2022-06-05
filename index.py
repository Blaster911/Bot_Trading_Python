from trade import Trade

# # TEST
priceETH = 2000
priceBTC = 28000
# priceUSDT = 1
# buy = 2000

# # My wallet
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
