from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

report = cg.get_coins_markets(vs_currency='usd')

int = int(input("Enter "))
count = 0
while int>count:
    print(report[count]['market_cap'],'-',report[count]['name'])
    count=count+1