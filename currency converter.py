from forex_python.converter import CurrencyRates

Currency = CurrencyRates()

amount = int(input("Enter the amount"))

from_currency = input("from_currency:").upper()
to_currency = input("to_currency:").upper()
print(from_currency, "to", to_currency,amount)
result = Currency.convert (from_currency,  to_currency,amount)
print(result)