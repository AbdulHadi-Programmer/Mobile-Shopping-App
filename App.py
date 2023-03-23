print("Welcome to Our Mobile Shopping App")
mobile = ["1) Google Pixel 3    price: 23000", "2) Google Pixel 3xl   price: 28000","3) Google Pixel 4   price: 36000", "4) Google Pixel 4xl  price: 45000", "5) Infinix hot 12   price: 55000","6) Infinix hot 10   price: 31000"]
rate = [23000, 28000, 36000, 45000, 55000, 31000]
customer = input("Enter your Name: ")
print("The Mobile that we are selling are: ")
for m in mobile:
    print(m)
    print()

def bill():
    print(f"\t•) The Bill:\n\tCustomer Name: {customer}\n\tProduct Name: {mobile[user-1]}\n\t17% GST Tax: {gst}\n\tTotal Cost: {cost}")

user = int(input("Which phone  do you want to buy : Type the num:-  "))

def decide():
    user1 = input("Add to Cart:-  Type Yes or No: ").lower()
    if  user1 == "yes":
        print(f"Your Selected mobile is: {mobile[user-1]}")
        bill()
    elif  user1 == "no":
        print("Exit")
    else:
        print("Thanks for using our App")

gst = int( rate[user-1] / 100 * 17 )
cost = int( rate[user-1] + gst )

if user == 1:
    decide()
elif user == 2:
    decide()
elif user == 3:
    decide()
elif user == 4:
    decide()
elif user == 5:
    decide()
elif user == 6:
    decide()
else:
    print("Wrong Input")
