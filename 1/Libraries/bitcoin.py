import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = response.json()
    bitcoin = price['bpi']['USD']['rate_float']
    amount = bitcoin * value
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit()
