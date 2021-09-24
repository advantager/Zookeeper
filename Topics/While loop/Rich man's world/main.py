deposit = float(input())
refundable_deposit = 700000
percentile = 7.1
years = 0
while deposit < refundable_deposit:
    years += 1
    deposit += deposit * percentile / 100
print(years)
