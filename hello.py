import json
import os

def display_options():
    print("\nOptions:")
    print("1. Record New Sales Information")
    print("2. Calculate Profit/Loss")
    print("3. Exit")

def get_new_sales_info():
    product = input("Enter the product name: ")
    quantity = int(input("Enter the quantity sold: "))
    price = float(input("Enter the price per unit: "))

    return {"product": product, "quantity": quantity, "price": price}

def calculate_profit_loss(sales_info):
    total_revenue = sum(item["quantity"] * item["price"] for item in sales_info)
    total_cost = float(input("Enter the total cost of products sold: "))
    profit_loss = total_revenue - total_cost

    print(f"\nTotal Revenue: {total_revenue}")
    print(f"Total Cost: {total_cost}")
    print(f"Profit/Loss: {profit_loss}")

    return profit_loss

def save_to_text_file(sales_info):
    with open("sales_records.txt", "w") as file:
        json.dump(sales_info, file)

def main():
    sales_info = []

    while True:
        display_options()
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            new_sale = get_new_sales_info()
            sales_info.append(new_sale)
            print("\nSales information recorded successfully!")

        elif choice == "2":
            if not sales_info:
                print("\nNo sales information recorded yet.")
            else:
                calculate_profit_loss(sales_info)

        elif choice == "3":
            save_to_text_file(sales_info)
            print("\nExiting the program. Sales information saved to 'sales_records.txt'.")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()