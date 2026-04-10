class KFC_System:
    def show_menu_card(self):
        print("\n" + "*"*10 + " KFC MENU CARD " + "*"*10)
        print(f"{'ID':<5} {'Item Name':<20} {'Price':<10}")
        print("-" * 35)
        for key, value in menu.items():
            print(f"{key:<5} {value[0]:<20} {value[1]:<10}")
        print("-" * 35)
class AdminView(KFC_System):
    def admin_menu(self):
        while True:
            print("\n--- ADMIN DASHBOARD ---")
            print("1. View Menu\n2. Add Item\n3. Remove Item\n4. Update Price\n5. Logout")
            choice = input("Select option: ")

            if choice == '1':
                self.show_menu_card()
            elif choice == '2':
                new_id = max(menu.keys()) + 1
                name = input("Enter item name: ")
                price = int(input("Enter price: "))
                menu[new_id] = [name, price]
                print(f"Item '{name}' added successfully!")
            elif choice == '3':
                self.show_menu_card()
                del_id = int(input("Enter Item ID to remove: "))
                if del_id in menu:
                    removed = menu.pop(del_id)
                    print(f"Removed: {removed[0]}")
                else:
                    print("Invalid ID.")
            elif choice == '4':
               self.show_menu_card()
               old_id = int(input("Enter the item ID:"))
               name = input("Enter the item name:")
               price = int(input("Enter the new or modify price:"))
               menu[old_id] = [name,price]
               print(f"Item '{name}' price updated successfully")
            elif choice == '5':
                break
class CustomerView(KFC_System):
    def __init__(self):
        self.cart = {}
        self.subtotal = 0
    def place_order(self):
        self.show_menu_card()
        while True:
            try:
                choice = int(input("Enter item ID to add (0 to finish): "))
                if choice == 0: break
                if choice in menu:
                    qty = int(input(f"Quantity for {menu[choice][0]}: "))
                    self.cart[choice] = self.cart.get(choice, 0) + qty
                else:
                    print("Invalid ID.")
            except ValueError:
                print("Please enter a valid number.")

    def generate_bill(self, name, num, add, ptype):
        if not self.cart:
            print("\nYour cart is empty!")
            return

        print("\n" + "*"*15 + " FINAL BILL " + "*"*15)
        print(f"Customer: {name} | Contact: {num}")
        print(f"Address: {add} | Payment: {ptype}")
        print("-" * 40)

        self.subtotal = 0
        for item_id, qty in self.cart.items():
            item_name, price = menu[item_id]
            total = price * qty
            self.subtotal += total
            print(f"{item_name:<20} x {qty:<3} = {total}")

        cgst = self.subtotal * 0.025
        sgst = self.subtotal * 0.025
        packaging = 30
        delivery = 40
        grand_total = self.subtotal + cgst + sgst + packaging + delivery

        print("-" * 40)
        print(f"Subtotal        : {self.subtotal:.2f}")
        print(f"GST (5%)        : {cgst + sgst:.2f}")
        print(f"Packaging/Deliv : {packaging + delivery}")
        print(f"TOTAL PAYABLE   : {grand_total:.2f}")
        print("-" * 40)
        self.track_order()

    def track_order(self):
        print("\nTracking your order...")
        stages = ["Order Placed", "Preparation", "Out for Delivery", "Delivered"]
        for stage in stages:
            time.sleep(1)
            print(f" >> {stage}...")
def main():
    while True:
        print("\n" + "#"*30)
        print("   WELCOME TO KFC VIRTUAL   ")
        print("#"*30)
        print("1. Admin Login\n2. Customer Login\n3. Exit")
        role = input("Choose your role: ")
        if role == '1':
            password = input("Enter Admin Password: ")
            if password == "kfc123":
                AdminView().admin_menu()
            else:
                print("Wrong Password!")

        elif role == '2':
            name = input("Name: ")
            num = input("Contact: ")
            add = input("Address: ")
            ptype = input("Payment Method: ")

            customer = CustomerView()
            customer.place_order()
            customer.generate_bill(name, num, add, ptype)
            print("\nThank you for choosing KFC!")

        elif role == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
