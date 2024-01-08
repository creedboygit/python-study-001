price_bag = int(input("가방의 가격은? >>> "))
price_watch = int(input("시계의 가격은? >>> "))

total_price = price_bag + price_watch

# print(total_price)

discount_str = ""
discounted_price = 0
discount_rate = 0

if total_price >= 100000:
    discount_rate = 30
# elif total_price >= 50000 & total_price < 100000:
# elif total_price >= 50000 and total_price < 100000:
# elif 50000 <= total_price < 100000:
elif 50000 <= total_price < 100000:
    discount_rate = 20
elif total_price < 50000:
    discount_rate = 10

discounted_price = total_price - (total_price * discount_rate / 100)

print("할인율 : " + str(discount_rate) + "% : " + str(discounted_price) + "원")
