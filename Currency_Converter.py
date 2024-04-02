from forex_python.converter import CurrencyRates
converter=CurrencyRates()
amount=int(input("enter the amount:"))
from_currency=input("enter to convert from:").upper()
to_currency=input("enter currency to convert to:").upper()
converted_amount = converter.convert(from_currency, to_currency, amount)
print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")
