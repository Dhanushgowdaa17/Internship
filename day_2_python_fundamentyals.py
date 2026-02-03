name = input("What is your name?")
current_age = input("What is your current age?")
current_age = int(current_age)
age_in_2030 = current_age + 4
print("Hello " + name + "! In 2030, you will be " + str(age_in_2030) + " years old.")


item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True
print("Item:", item_name, "Qty:", quantity, "Price:", price, "Available:", in_stock)
total_cost = quantity * price
print("Total Cost:", total_cost)


total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
share_per_person = total_bill / people
print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")
print(type(total_bill))
print(type(people))
print(type(share_per_person))