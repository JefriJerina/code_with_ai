import pyautogui
import time

def shopping_bill_calculator():
    """
    Shopping Bill Calculator using PyAutoGUI keyboard operations
    Calculates total cost of 3 items including tax percentage
    """
    
    # Disable PyAutoGUI failsafe (optional - remove if you want failsafe)
    pyautogui.FAILSAFE = True
    
    # Add delay between operations for better visibility
    pyautogui.PAUSE = 1
    
    print("Shopping Bill Calculator")
    print("=" * 30)
    
    # Sample data for demonstration
    items = [
        {"name": "Laptop", "price": 899.99},
        {"name": "Mouse", "price": 25.50},
        {"name": "Keyboard", "price": 75.00}
    ]
    
    tax_percentage = 8.5  # 8.5% tax
    
    print("Items to calculate:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['name']}: ${item['price']:.2f}")
    
    print(f"\nTax Rate: {tax_percentage}%")
    print("\nStarting automated calculation in 3 seconds...")
    print("Make sure your text editor or calculator is open and focused!")
    
    # Countdown
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    print("Starting automation...\n")
    
    # Calculate subtotal
    subtotal = sum(item['price'] for item in items)
    
    # Type the bill header
    pyautogui.typewrite("SHOPPING BILL CALCULATION")
    pyautogui.press('enter')
    pyautogui.typewrite("=" * 30)
    pyautogui.press('enter', presses=2)
    
    # Type each item
    pyautogui.typewrite("ITEMS:")
    pyautogui.press('enter')
    
    for i, item in enumerate(items, 1):
        item_line = f"{i}. {item['name']}: ${item['price']:.2f}"
        pyautogui.typewrite(item_line)
        pyautogui.press('enter')
    
    pyautogui.press('enter')
    
    # Calculate and type subtotal
    pyautogui.typewrite(f"Subtotal: ${subtotal:.2f}")
    pyautogui.press('enter')
    
    # Calculate tax amount
    tax_amount = subtotal * (tax_percentage / 100)
    pyautogui.typewrite(f"Tax ({tax_percentage}%): ${tax_amount:.2f}")
    pyautogui.press('enter')
    
    # Calculate total
    total = subtotal + tax_amount
    pyautogui.typewrite("-" * 25)
    pyautogui.press('enter')
    pyautogui.typewrite(f"TOTAL: ${total:.2f}")
    pyautogui.press('enter', presses=2)
    
    # Type summary
    pyautogui.typewrite("CALCULATION SUMMARY:")
    pyautogui.press('enter')
    pyautogui.typewrite(f"Number of items: {len(items)}")
    pyautogui.press('enter')
    pyautogui.typewrite(f"Subtotal: ${subtotal:.2f}")
    pyautogui.press('enter')
    pyautogui.typewrite(f"Tax Amount: ${tax_amount:.2f}")
    pyautogui.press('enter')
    pyautogui.typewrite(f"Final Total: ${total:.2f}")
    
    print("Automation completed!")
    print(f"\nCalculation Results:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")

def interactive_shopping_bill():
    """
    Interactive version that takes user input and then uses PyAutoGUI
    """
    print("Interactive Shopping Bill Calculator")
    print("=" * 40)
    
    items = []
    
    # Get item details from user
    for i in range(3):
        print(f"\nEnter details for item {i+1}:")
        name = input("Item name: ")
        while True:
            try:
                price = float(input("Item price: $"))
                break
            except ValueError:
                print("Please enter a valid price!")
        
        items.append({"name": name, "price": price})
    
    # Get tax percentage
    while True:
        try:
            tax_percentage = float(input("\nEnter tax percentage (e.g., 8.5 for 8.5%): "))
            break
        except ValueError:
            print("Please enter a valid tax percentage!")
    
    # Calculate totals
    subtotal = sum(item['price'] for item in items)
    tax_amount = subtotal * (tax_percentage / 100)
    total = subtotal + tax_amount
    
    print(f"\nCalculation Preview:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_percentage}%): ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
    
    input("\nPress Enter to start typing the bill (make sure text editor is focused)...")
    
    # Use PyAutoGUI to type the results
    pyautogui.PAUSE = 0.5
    
    # Type the complete bill
    pyautogui.typewrite("SHOPPING BILL")
    pyautogui.press('enter')
    pyautogui.typewrite("=" * 20)
    pyautogui.press('enter', presses=2)
    
    pyautogui.typewrite("ITEMS PURCHASED:")
    pyautogui.press('enter')
    
    for i, item in enumerate(items, 1):
        pyautogui.typewrite(f"{i}. {item['name']}: ${item['price']:.2f}")
        pyautogui.press('enter')
    
    pyautogui.press('enter')
    pyautogui.typewrite(f"Subtotal: ${subtotal:.2f}")
    pyautogui.press('enter')
    pyautogui.typewrite(f"Tax ({tax_percentage}%): ${tax_amount:.2f}")
    pyautogui.press('enter')
    pyautogui.typewrite("-" * 20)
    pyautogui.press('enter')
    pyautogui.typewrite(f"TOTAL: ${total:.2f}")
    
    print("\nBill typed successfully!")

if __name__ == "__main__":
    print("Shopping Bill Calculator with PyAutoGUI")
    print("=" * 50)
    print("1. Demo mode (predefined items)")
    print("2. Interactive mode (enter your own items)")
    
    choice = input("\nSelect option (1 or 2): ")
    
    if choice == "1":
        shopping_bill_calculator()
    elif choice == "2":
        interactive_shopping_bill()
    else:
        print("Invalid choice! Running demo mode...")
        shopping_bill_calculator()