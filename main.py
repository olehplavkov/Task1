btc = float(input("How many $ costs 1 BTC today?  "))
money = float(input("How many $ do you have?  "))
def crypt(btc, money):
    return money / btc
    print("You can buy " + crypt + "BTC!")
print("You can buy " + str(crypt(money, btc)) + " BTC")
