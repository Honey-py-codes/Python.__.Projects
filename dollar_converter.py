# 💵 Rupees to Dollar Converter

# 1 USD = 84.5 INR (approx) — tu chahe to latest rate daal sakta hai
usd_rate = 84.5

# User se input lo
rupees = float(input("Enter amount in Indian Rupees (₹): "))

# Conversion
dollars = rupees / usd_rate

# Result show karo
print(f"💰 {rupees:.2f} INR = ${dollars:.2f} USD")

 