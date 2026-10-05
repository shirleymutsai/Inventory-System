
def run_inventory_system():
    inventory = {}
    audit_trail = []

    print("--- Inventory System ---")

    while True:
        print("\n[1] Add New Asset")
        print("[2] Update Asset (Stock & Price)")
        print("[3] Search for Asset")
        print("[4] View Summary Table")
        print("[5] Exit")

        choice = input("Select option (1-5): ")

        if choice == '1':
            name = input("Enter asset name: ").strip().title()
            if name in inventory:
                print(f"Asset '{name}' already exists. Use 'Update Asset' to change values.")
                continue
            try:
                units = int(input(f"Enter initial units for {name}: "))
                price = float(input(f"Enter value per unit: "))
                inventory[name] = {'units': units, 'price': price}
                audit_trail.append(f"INITIALIZED: {name} | Qty: {units} | Price: {price}")
                print(f"Success: {name} added to ledger.")
            except ValueError:
                print("Error: Please enter numeric values for units and price.")

        elif choice == '2':
            name = input("Enter asset name to update: ").strip().title()
            if name not in inventory:
                print("Asset not found.")
            else:
                print(f"\nEditing {name}: {inventory[name]['units']} units @ ${inventory[name]['price']:,.2f}")
                print("What would you like to update?")
                print("[A] Change Stock Level (Add/Subtract)")
                print("[B] Change Unit Price")
                print("[C] Cancel")

                sub_choice = input("Select A, B, or C: ").upper()

                if sub_choice == 'A':
                    try:
                        change = int(input("Enter change amount (e.g., '10' for more, '-5' for less): "))
                        inventory[name]['units'] += change
                        audit_trail.append(f"STOCK CHANGE: {name} by {change} units.")
                        print(f"Update Successful. New Stock: {inventory[name]['units']}")
                    except ValueError:
                        print("Error: Please enter a whole number.")

                elif sub_choice == 'B':
                    try:
                        new_price = float(input(f"Enter NEW unit price for {name}: "))
                        inventory[name]['price'] = new_price
                        audit_trail.append(f"PRICE CHANGE: {name} to ${new_price}")
                        print(f"Update Successful. New Price: ${inventory[name]['price']:,.2f}")
                    except ValueError:
                        print("Error: Please enter a numeric value.")

                elif sub_choice == 'C':
                    print("Update cancelled.")
                else:
                    print("Invalid selection.")
        elif choice == '3':
            search_name = input("Enter the name of the asset to search: ").strip().title()
            if search_name in inventory:
                data = inventory[search_name]
                print("\n" + "-"*40)
                print(f"SEARCH RESULT FOR: {search_name}")
                print(f"Units in Stock:  {data['units']}")
                print(f"Value Per Unit:  ${data['price']:,.2f}")
                print(f"Total Asset Val: ${(data['units'] * data['price']):,.2f}")
                print("-"*40)
            else:
                print(f"Record for '{search_name}' not found.")

        elif choice == '4':
            if not inventory:
                print("\nLedger is empty.")
            else:
                print("\n" + "="*75)
                print(f"{'ASSET NAME':<20} | {'UNITS':<10} | {'VALUE/UNIT':<15} | {'TOTAL VALUE':<15}")
                print("-" * 75)
                grand_total = 0
                for name, data in inventory.items():
                    total_val = data['units'] * data['price']
                    print(f"{name:<20} | {data['units']:<10} | ${data['price']:<14,.2f} | ${total_val:<14,.2f}")
                    grand_total += total_val
                print("-" * 75)
                print(f"{'PORTFOLIO TOTAL':<49} | ${grand_total:,.2f}")
                print("="*75)

        elif choice == '5':
            print("System finalized. Total transactions logged:", len(audit_trail))
            break

run_inventory_system()