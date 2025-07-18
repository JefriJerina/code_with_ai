# Even or Odd Checker with PyAutoGUI
import pyautogui
import time

def check_even_odd(number):
    """Check if a number is even or odd"""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def check_list(numbers):
    """Check a list of numbers and return results"""
    results = []
    for num in numbers:
        result = check_even_odd(num)
        results.append(f"{num} is {result}")
    return results

def display_popup_results(number, result):
    """Display results using PyAutoGUI popup"""
    message = f"The number {number} is {result}!"
    pyautogui.alert(message, title="Even/Odd Result")

def display_list_results(numbers, results):
    """Display list results in a popup"""
    message = "Even/Odd Results:\n\n"
    for i, num in enumerate(numbers):
        result = check_even_odd(num)
        message += f"{num} is {result}\n"
    
    # Add summary
    even_count = sum(1 for num in numbers if check_even_odd(num) == "even")
    odd_count = len(numbers) - even_count
    message += f"\nSummary:\nEven numbers: {even_count}\nOdd numbers: {odd_count}"
    
    pyautogui.alert(message, title="List Results")

def interactive_mode():
    """Interactive mode using PyAutoGUI input"""
    while True:
        try:
            # Get user input using PyAutoGUI
            user_input = pyautogui.prompt("Enter a number to check (or 'quit' to exit):", 
                                        title="Even/Odd Checker")
            
            if user_input is None or user_input.lower() == 'quit':
                pyautogui.alert("Thanks for using the Even/Odd Checker!", title="Goodbye")
                break
            
            number = int(user_input)
            result = check_even_odd(number)
            display_popup_results(number, result)
            
        except ValueError:
            pyautogui.alert("Please enter a valid number!", title="Error")
        except Exception as e:
            pyautogui.alert(f"An error occurred: {str(e)}", title="Error")
            break

def automated_demo():
    """Automated demonstration using PyAutoGUI"""
    pyautogui.alert("Starting automated demo!\nThe program will automatically check numbers.", 
                   title="Demo Mode")
    
    demo_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for num in demo_numbers:
        result = check_even_odd(num)
        message = f"Checking number: {num}\nResult: {num} is {result}"
        pyautogui.alert(message, title=f"Demo - Number {num}")
        time.sleep(1)  # Small delay between popups
    
    pyautogui.alert("Demo complete!", title="Demo Finished")

# Main program
def main():
    print("Even or Odd Checker with PyAutoGUI")
    print("-" * 35)
    
    # Check single number with popup
    number = 7
    print(f"Checking single number: {number}")
    result = check_even_odd(number)
    print(f"{number} is {result}")
    display_popup_results(number, result)
    
    # Check a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nChecking list: {numbers}")
    
    results = check_list(numbers)
    for result in results:
        print(result)
    
    # Display list results in popup
    display_list_results(numbers, results)
    
    # Ask user what they want to do next
    choice = pyautogui.confirm("What would you like to do next?", 
                              title="Choose Action",
                              buttons=["Interactive Mode", "Automated Demo", "Exit"])
    
    if choice == "Interactive Mode":
        interactive_mode()
    elif choice == "Automated Demo":
        automated_demo()
    else:
        pyautogui.alert("Thanks for using the Even/Odd Checker!", title="Goodbye")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        pyautogui.alert(f"An error occurred: {str(e)}", title="Error")