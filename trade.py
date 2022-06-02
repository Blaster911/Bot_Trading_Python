# TEST

buy = 25000
pourcentage = 2
priceToken = 300
quantityBuy = 30
quantityToken = quantityBuy/priceToken
print(quantityToken)

# while True:
#     price = input("Rentrer le prix :")
#     calcBuyUp = buy + (buy * pourcentage / 100)
#     calcBuyDown = buy - (buy * pourcentage / 100)

#     if(float(price) <= calcBuyUp):
#         print("non. prix d'achat minimum : " + str(calcBuyUp))
#     if(float(price) > calcBuyUp):
#         priceBuy = float(price)
#         moy = (priceBuy + buy)/2
#         print("Acheter à : " + str(moy))