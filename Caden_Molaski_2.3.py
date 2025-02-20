print("Apples are $0.50 today and Pineapples are $1.25 today")
num_apples = float(input("How many Apples would you like to buy?"))
num_pineapples = float(input("How many Pineapples would you like to buy?"))
apple_price = num_apples*0.50
pineapple_price = num_pineapples*1.25
total_sum = (pineapple_price+apple_price)
print(f"That will be ${total_sum:.2f} please")