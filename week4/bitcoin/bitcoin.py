import sys
import requests

# check cmdline args
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    btc = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
price = response["bpi"]["USD"]["rate_float"]
cost = btc * price
print(f"${cost:,.4f}")
